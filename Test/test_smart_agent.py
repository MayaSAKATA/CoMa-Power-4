# test_smart_agent.py

import unittest
import numpy as np
import random
class MockActionSpace:
    """ 
    Simulate action_sace needed for SmartAgent initialization.
    """
    def __init__(self):
        pass 

class MockEnvironment:
    """
    Simulate l'environnement PettingZoo requis par SmartAgent.__init__.
    """    
    agents = ["player_0", "player_1"]
    
    def action_space(self, agent_name):
        return MockActionSpace()


# SmartAgent Class to test : 
class SmartAgent:
    """
    A rule-based agent that plays strategically
    """

    def __init__(self, env, player_name=None):
        """
        Initialize the smart agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional name for the agent
        """
        self.env = env
        self.action_space = env.action_space(env.agents[0])
        self.player_name = player_name or "SmartAgent"

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose an action using rule-based strategy

        Strategy priority:
        1. Win if possible
        2. Block opponent from winning
        3. Play center if available
        4. Random valid move
        """
        # Get valid actions
        valid_actions = self._get_valid_actions(action_mask)

        # Rule 1: Try to win
        winning_move = self._find_winning_move(observation, valid_actions, channel=0)
        if winning_move is not None:
            return winning_move

        # Rule 2: Block opponent
        blocking_move = self._find_winning_move(observation, valid_actions, channel=1)
        if blocking_move is not None:
            return blocking_move

        # Rule 3: Prefer center
        if 3 in valid_actions:
            return 3

        # Rule 4: Random fallback
        return random.choice(valid_actions)

    def _get_valid_actions(self, action_mask):
        """
        Get list of valid column indices

        Parameters:
            action_mask: numpy array (7,) with 1 for valid, 0 for invalid

        Returns:
            list of valid column indices
        """

        return [i for i, valid in enumerate(action_mask) if valid == 1]

    def _find_winning_move(self, observation, valid_actions, channel):
        """
        Find a move that creates 4 in a row for the specified player

        Parameters:
            observation: numpy array (6, 7, 2) - current board state
            valid_actions: list of valid column indices
            channel: 0 for current player, 1 for opponent

        Returns:
            column index (int) if winning move found, None otherwise
        """

        for col in valid_actions:
            next_row = self._get_next_row(observation, col)
            if next_row is not None:
                if self._check_win_from_position(observation, next_row, col, channel):
                    return col
        return None

    def _get_next_row(self, board, col):
        """
        Find which row a piece would land in if dropped in column col

        Parameters:
            board: numpy array (6, 7, 2)
            col: column index (0-6)

        Returns:
            row index (0-5) if space available, None if column full
        """

        for row in range(5, -1, -1):  # Start from bottom (row 5)
            if board[row, col, 0] == 0 and board[row, col, 1] == 0:
                return row  # This position is empty
        return None  # Column is full


    def _check_win_from_position(self, board, row, col, channel):
        """
        Check if placing a piece at (row, col) would create 4 in a row

        Parameters:
            board: numpy array (6, 7, 2)
            row: row index (0-5)
            col: column index (0-6)
            channel: 0 or 1 (which player's pieces to check)

        Returns:
            True if this position creates 4 in a row/col/diag, False otherwise
        """

        board[row, col, channel] = 1 # place the piece at (row, col)

        direction = [(0, 1), (1, 0), (1, -1), (1, 1)]
        for dr, dc in direction:
            count = 1 # counts pieces in a row, start at 1 -> placement at (row,col)
            for i in range(1, 4): # forward
                r = row + dr * i
                c = col + dc * i
                if 0 <= r < 6 and 0 <= c  < 7 and board[r, c, channel]==1: # Check board bounds and if pieces are ours
                    count += 1
                else :
                    break
            for i in range(1, 4): # backward
                r = row - dr * i
                c = col - dc * i
                if 0 <= r < 6 and 0 <= c  < 7 and board[r, c, channel]==1: # Check board bounds and if pieces are ours
                    count += 1
                else :
                    break
            
            if count >= 4: # Found at least 4 in a row
                return True
            
        board[row, col, channel] = 0 # undo placement piece at (row, col)
        return False

class TestSmartAgent(unittest.TestCase):
    def setUp(self):
        """
        Initializes the agent by providing it with the required dummy environment.
        """

        mock_env = MockEnvironment()
    
        self.agent = SmartAgent(mock_env)
        

    def test_get_valid_actions(self):
        """ 
        Method test _get_valid_actions 

        Test when all columns are valid and when only odd columns are valid 
        """
        agent = self.agent
        mask = [1, 1, 1, 1, 1, 1, 1]  # All columns valid
        assert agent._get_valid_actions(mask) == [0, 1, 2, 3, 4, 5, 6]

        mask = [0, 1, 0, 1, 0, 1, 0]  # Only odd columns
        assert agent._get_valid_actions(mask) == [1, 3, 5]

    def test_get_next_row(self): 
        """
        Method test _get_nest_row 
        
        Test in case of empty board and of column with one piece 
        """

        agent = self.agent
        # Empty board - piece goes to bottom
        board = np.zeros((6, 7, 2))
        assert agent._get_next_row(board, 3) == 5

        # Column with one piece - next piece goes on top
        board[5, 3, 0] = 1
        assert agent._get_next_row(board, 3) == 4

    def test_find_winning_move(self):

        """
        Method test _find_winning_move

        Test in case of victory in column and in increase diagonal 
        and in case of block opponent from victory in row and decrease diagonal
        """

        agent = self.agent
        valid_actions = [0, 1, 2, 3, 4, 5, 6]

        #case 1 : win on a column (here is the first column)

        vertical=np.zeros((6,7,2),dtype=int) #create an empty board
        #place 3 pieces on column 1 for the current agent 
        vertical[5,0,0] = 1
        vertical[4,0,0] = 1 
        vertical[3,0,0] = 1


        winning_move = agent._find_winning_move(vertical, valid_actions, channel=0)
        self.assertEqual(winning_move, 0)

        #case 2 : Block opponent from winning, on a row 

        horizontal=np.zeros((6,7,2),dtype=int)
        #place 3 pieces on row 5, for opponent player
        horizontal[5,3,1]=1
        horizontal[5,4,1] =1
        horizontal[5,5,1]=1

        horizontal[5,2,0]=1

        blocking_move = agent._find_winning_move(horizontal, valid_actions, channel=1)
        self.assertEqual(blocking_move, 6)

        #case 3 : victory in an increasing diagonal

        indiag = np.zeros((6,7,2),dtype=int)
        #set pieces for current player
        indiag[5,0,0]=1
        indiag[4,1,0]=1
        indiag[3,2,0]=1
        indiag[4,3,0]=1

        #set pieces for opponent player 
        indiag[5,1,1] = 1
        indiag[5,2,1] = 1
        indiag[5,3,1] = 1
        indiag[4,2,1] = 1
        indiag[3,3,1] = 1


        winning_move = agent._find_winning_move(indiag, valid_actions, channel=0)
        self.assertEqual(winning_move, 3)

        #case 4: block opponent from winning on a decreasing diagonal

        dediag = np.zeros((6,7,2),dtype=int)

        dediag[5,0,0] = 1
        dediag[5,2,0] = 1
        dediag[3,0,0] = 1
        dediag[4,0,0] = 1

        dediag[5,1,1] = 1
        dediag[4,0,1] = 1
        dediag[2,0,1] = 1
        dediag[3,1,1] = 1
        dediag[4,2,1] = 1

        blocking_move = agent._find_winning_move(dediag, valid_actions, channel=1)
        self.assertEqual(blocking_move, 3)

    
    def test_check_win_from_position(self):

        """
        Method test _check_win_from_position

        Test in case of victory in row, column, increase and decrease diagonal, 
        in case of no victory and blockage by the opponent 
        """

        agent = self.agent
        valid_actions = [0, 1, 2, 3, 4, 5, 6]
        
        #case 1: win in row 

        board = np.zeros((6,7,2), dtype = int)

        board[5,0,0] = 1
        board[5,1,0] = 1
        board[5,3,0] = 1

        row=5
        col=2
        self.assertTrue(agent._check_win_from_position(board, row, col, channel =0))  

        #case 2: win in column 

        board = np.zeros((6,7,2), dtype=int)

        board[5,0,0] = 1 
        board[4,0,0] = 1 
        board[3,0,0] = 1 

        row = 2
        col = 0
        self.assertTrue(agent._check_win_from_position(board, row, col, channel =0))

        #case 3 : win in an increase diagonal 

        board = np.zeros((6,7,2), dtype=int)

        board[2,3,0] = 1 
        board[3,2,0] = 1 
        board[4,1,0] = 1 

        row = 5
        col = 0
        self.assertTrue(agent._check_win_from_position(board, row, col, channel =0))


        #case 4 : win in an decrease diagonal 

        board = np.zeros((6,7,2), dtype=int)

        board[2,0,0] = 1 
        board[5,3,0] = 1 
        board[4,2,0] = 1 

        row = 3
        col = 1
        self.assertTrue(agent._check_win_from_position(board, row, col, channel =0))

        #case 5 : no win 

        board = np.zeros((6,7,2), dtype=int)

        board[2,0,0] = 1 
        board[5,3,0] = 1 
        board[4,2,0] = 1 

        row = 5
        col = 4 
        self.assertFalse(agent._check_win_from_position(board, row, col, channel =0))

        #case 6 : block by the opponent 

        board = np.zeros((6,7,2), dtype=int)

        board[5,0,0] = 1
        board[5,1,1] = 1
        board[5,2,0] = 1

        row = 5 
        col = 3 
        self.assertFalse(agent._check_win_from_position(board, row, col, channel =0))

if __name__ == '__main__':
    unittest.main()

