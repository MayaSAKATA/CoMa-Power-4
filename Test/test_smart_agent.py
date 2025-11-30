# test_smart_agent.py

import unittest
import numpy as np
import random

from src.smart_agent import SmartAgent

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

