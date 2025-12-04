"""
Minimax agent with alpha-beta pruning
"""
from pettingzoo.classic import connect_four_v3
from tqdm import tqdm
from tournament import run_tournament
from smart_agent import SmartAgent

import numpy as np
import random
import time


class MinimaxAgent:
    """
    Agent using minimax algorithm with alpha-beta pruning
    """

    def __init__(self, env, depth=4, player_name=None):
        """
        Initialize minimax agent

        Parameters:
            env: PettingZoo environment
            depth: How many moves to look ahead
            player_name: Optional name
        """
        self.env = env
        self.action_space = env.action_space(env.agents[0])
        self.depth = depth
        self.player_name = player_name or f"Minimax(d={depth})"

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose action using minimax algorithm
        """
        valid_actions = [i for i, valid in enumerate(action_mask) if valid == 1]

        best_action = None
        best_value = float('-inf')

        # Try each valid action
        for action in valid_actions:
            # Simulate the move
            new_board = self._simulate_move(observation, action, channel=0)

            # Evaluate using minimax (opponent's turn, so minimizing)
            value = self._minimax(new_board, self.depth - 1, float('-inf'), float('inf'), False)

            if value > best_value:
                best_value = value
                best_action = action

        return best_action if best_action is not None else random.choice(valid_actions)

    def _minimax(self, board, depth, alpha, beta, maximizing):
        """
        Minimax algorithm with alpha-beta pruning

        Parameters:
            board: Current board state
            depth: Remaining depth to search
            alpha: Best value for maximizer
            beta: Best value for minimizer
            maximizing: True if maximizing player's turn

        Returns:
            float: evaluation score
        """
        # TODO: Implement minimax
        # Base cases:
        #   - depth == 0: return evaluate(board)
        #   - game over: return win/loss score

        # Recursive case:
        #   - Try all valid moves
        #   - Recursively evaluate
        #   - Update alpha/beta
        #   - Prune if possible

        # Base case 1: Check if game is over
        if self._check_win(board, 0):  # We won
            return 10000 + depth  # Prefer faster wins
        if self._check_win(board, 1):  # Opponent won
            return -10000 - depth  # Prefer slower losses
        
        # Base case 2: Maximum depth reached
        if depth == 0:
            return self._evaluate(board)
        
        # Base case 3 : board full (draw)
        valid_moves = self._get_valid_moves(board)
        
        # Recursive case: maximizing player (us)
        if maximizing:
            max_eval = float('-inf')
            for move in valid_moves:
                new_board = self._simulate_move(board, move, channel=0)
                eval = self._minimax(new_board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Beta cutoff
            return max_eval
        
        # Recursive case: minimizing player (opponent)
        else:
            min_eval = float('inf')
            for move in valid_moves:
                new_board = self._simulate_move(board, move, channel=1)
                eval = self._minimax(new_board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Alpha cutoff
            return min_eval

    def _simulate_move(self, board, col, channel):
        """
        Simulate placing a piece without modifying original board

        Parameters:
            board: Current board (6, 7, 2)
            col: Column to play
            channel: 0 for current player, 1 for opponent

        Returns:
            new_board: Copy of board with move applied
        """
        # TODO: Implement
        # 1. Copy board
        # 2. Find next available row in column
        # 3. Place piece
        # 4. Return new board
        new_board = board.copy()

        for row in range(5, -1, -1):  # Start from bottom (row 5)
            if new_board[row, col, 0] == 0 and new_board[row, col, 1] == 0:
                new_board[row, col, channel] = 1
                break
        
        return new_board

    def _get_valid_moves(self, board):
        """
        Get list of valid column indices

        Returns:
            list of valid columns
        """
        # TODO: Check which columns aren't full
        valid_moves = []
        for col in range(7):
            # Check if top row is empty
            if board[0, col, 0] == 0 and board[0, col, 1] == 0:
                valid_moves.append(col)
        return valid_moves
    
    def _evaluate_window(self, window):
        """
        Evaluate a window of 4 positions
        Parameters:
            window: numpy array of shape (4, 2)
        Returns:
            float: score for this window
        """
        our_pieces = np.sum(window[:, 0])
        opp_pieces = np.sum(window[:, 1])
        
        # If both players have pieces, no threat
        if our_pieces > 0 and opp_pieces > 0:
            return 0
        
        # Score based on our pieces
        if our_pieces == 4:
            return 100
        elif our_pieces == 3:
            return 5
        elif our_pieces == 2:
            return 2
        
        # Penalty for opponent's pieces
        if opp_pieces == 3:
            return -4
        elif opp_pieces == 2:
            return -1
        
        return 0

    def _evaluate(self, board):
        """
        Evaluate board position

        Returns:
            float: score (positive = good for us)
        """
        # TODO: Implement evaluation function
        # Consider: wins, threats, position, etc.
        score = 0
        
        # Evaluate all possible windows of 4
        # Horizontal
        for row in range(6):
            for col in range(4):
                window = board[row, col:col+4, :]
                score += self._evaluate_window(window)
        
        # Vertical
        for row in range(3):
            for col in range(7):
                window = board[row:row+4, col, :]
                score += self._evaluate_window(window)
        
        # Diagonal (increasing)
        for row in range(3):
            for col in range(4):
                window = np.array([board[row+i, col+i, :] for i in range(4)])
                score += self._evaluate_window(window)
        
        # Diagonal (decreasing)
        for row in range(3, 6):
            for col in range(4):
                window = np.array([board[row-i, col+i, :] for i in range(4)])
                score += self._evaluate_window(window)
        
        # Center column preference
        center_col = board[:, 3, 0]
        center_count = np.sum(center_col)
        score += center_count * 3
        
        return score

    def _check_win(self, board, channel):
        """
        Check if player has won

        Returns:
            bool: True if won
        """
        # TODO: Check all positions for 4 in a row
        # Horizontal
        for row in range(6):
            for col in range(4):
                if np.all(board[row, col:col+4, channel] == 1):
                    return True
        
        # Vertical
        for row in range(3):
            for col in range(7):
                if np.all(board[row:row+4, col, channel] == 1):
                    return True
        
        # Diagonal (increasing)
        for row in range(3):
            for col in range(4):
                if all(board[row+i, col+i, channel] == 1 for i in range(4)):
                    return True
        
        # Diagonal (decreasing)
        for row in range(3, 6):
            for col in range(4):
                if all(board[row-i, col+i, channel] == 1 for i in range(4)):
                    return True
        
        return False


if __name__ == "__main__":
    depths=[2, 3, 4, 5, 6]
    results_summary = []


    for depth in tqdm(depths, desc="Testing depths", unit="depth"):
        env = connect_four_v3.env()
        env.reset()

        agent = MinimaxAgent(env, depth=depth)
        times = []
        for _ in tqdm(range(5), desc=f"Measuring time (depth={depth})", leave=False):
            env.reset()
            observation, _, _, _, _ = env.last()
            
            start = time.time()
            agent.choose_action(observation["observation"],action_mask=observation["action_mask"])
            times.append(time.time() - start)
        
        avg_time = sum(times) / len(times)
    
        # Temporary class with new depth
        class MinimaxDepthN(MinimaxAgent):
                def __init__(self, env):
                    super().__init__(env, depth=depth)
        # Run tournament
        agents = [MinimaxDepthN, SmartAgent]
        results = run_tournament(agents, n_games=5)

        results_summary.append({"depth": depth,"avg_time": avg_time,"wins": results["wins"],"losses": results["losses"],
                                "draws": results["draws"]})

    print("\nSummary of results:")
    for res in results_summary:
        print(f"Depth {res["depth"]}: Avg Time: {res["avg_time"]:.4f}s, Wins: {res["wins"]}, Losses: {res["losses"]}, Draws: {res["draws"]}")


# Summary of results:
# Depth 2: Avg Time: 0.0348s, Wins: 5, Losses: 0, Draws: 0
# Depth 3: Avg Time: 0.1744s, Wins: 5, Losses: 0, Draws: 0
# Depth 4: Avg Time: 0.8172s, Wins: 5, Losses: 0, Draws: 0
# Depth 5: Avg Time: 3.8324s, Wins: 5, Losses: 0, Draws: 0
# Depth 6: Avg Time: 14.2014s, Wins: 5, Losses: 0, Draws: 0