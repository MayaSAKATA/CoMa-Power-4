# test_suite.py

import unittest
import numpy as np
import random

import time
import tracemalloc

from pettingzoo.classic import connect_four_v3
from src.smart_agent import SmartAgent
from src.random_agent import RandomAgent
from test_smart_vs_random import play_game_rvs, play_multiple_games


# Mock Random Agent for testing purposes (independent test)
class RandomAgent:
    def __init__(self, env):
        self.env = env
    
    def choose_action(self, observation, action_mask):
        valid_actions = [i for i, valid in enumerate(action_mask) if valid == 1]
        return random.choice(valid_actions)
    

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        """
        Initializes the agent by providing it with the required environment.
        """
        self.env = connect_four_v3.env()
        self.env.reset()
        self.agent = SmartAgent(self.env)

    def test_scenario1_winning_move(self):
        """
        Test that the agent takes the winning move when available.
        """
        
        obs = np.zeros((6, 7, 2), dtype=np.int8) # create an empty board
        obs[5, 0, 0] = 1 # place player 0 pieces
        obs[5, 1, 0]= 1
        obs[5, 2, 0]= 1

        mask = np.ones(7, dtype=np.int8) # all actions valid
        action = self.agent.choose_action(obs, action_mask=mask)
        self.assertEqual(action, 3, "Agent should play col 3")

    def test_scenario2_blocking_move(self):
        """
        Test that the agent blocks opponent's winning move when necessary.
        """ 
        
        obs = np.zeros((6, 7, 2), dtype=np.int8) # create an empty board
        obs[5, 0, 1] = 1 # place opponent's pieces
        obs[5, 1, 1]= 1
        obs[5, 2, 1]= 1

        mask = np.ones(7, dtype=np.int8) # all actions valid
        action = self.agent.choose_action(obs, action_mask=mask)
        self.assertEqual(action, 3, "Agent should play col 3 to block opponent")
    
    def test_scenario3_split_win(self):
        """
        Test that the agent takes the winning move when available in a different scenario.
        """
        
        obs = np.zeros((6, 7, 2), dtype=np.int8) # create an empty board
        obs[5, 0, 0] = 1 # place player 0 pieces
        obs[5, 1, 0]= 1
        obs[5, 3, 0]= 1

        mask = np.ones(7, dtype=np.int8) # all actions valid
        action = self.agent.choose_action(obs, action_mask=mask)
        self.assertEqual(action, 2, "Agent should play col 2 to win")

    def test_scenario4_blocking_move(self):
        """
        Test that the agent blocks opponent's winning move in a different scenario."""
        
        obs = np.zeros((6, 7, 2), dtype=np.int8) # create an empty board
        obs[5, 0, 1] = 1 # place opponent's pieces
        obs[5, 1, 1]= 1
        obs[5, 3, 1]= 1
        obs[5, 4, 1]= 1

        mask = np.ones(7, dtype=np.int8) # all actions valid
        action = self.agent.choose_action(obs, action_mask=mask)
        self.assertEqual(action, 2, "Agent should play col 2 to block opponent")

    def test_scenario5_winning_over_blocking_move(self):
        """
        Test that the agent prefers winning move over blocking opponent.
        """
        
        obs = np.zeros((6, 7, 2), dtype=np.int8) # create an empty board
                
        obs[5, 0, 0] = 1 # place player 1 pieces
        obs[5, 1, 0]= 1
        obs[5, 2, 0]= 1

        obs[5, 0, 1] = 1 # place opponent's pieces
        obs[5, 1, 1]= 1
        obs[5, 2, 1]= 1

        mask = np.ones(7, dtype=np.int8) # all actions valid
        action = self.agent.choose_action(obs, action_mask=mask)
        self.assertEqual(action, 3, "Agent should play col 3 to block opponent")

class TestPerformanceAndTournament(unittest.TestCase):
    def setUp(self):
        """
        Initializes the environment and agents for performance and tournament tests.
        """
        self.env = connect_four_v3.env()
        self.env.reset()
        self.smart_agent = SmartAgent(self.env)
        self.random_agent = RandomAgent(self.env)

    def test_performance_time(self):
        """
        Test the performance of the SmartAgent in terms of execution time.
        """

        self.env.reset()
        obs, _, _, _, _ = self.env.last()
        mask = np.array([1, 1, 1, 1, 1, 1, 1], dtype=np.int8)
        
        start_time = time.time()
        for _ in range(100):
            self.smart_agent.choose_action(obs["observation"], action_mask=mask)
        end_time = time.time()
        
        avg_time = (end_time - start_time) / 100
        print(f"  Average action time : {avg_time:.6f} seconds")
        self.assertLess(avg_time, 3, "The agent is too slow (> 3s per action)")
        
    def test_performance_memory(self):
            """
            Test the performance of the SmartAgent in terms of memory.
            """
            self.env.reset()
            obs, _, _, _, _ = self.env.last()
            mask = np.array([1, 1, 1, 1, 1, 1, 1], dtype=np.int8)
            
            tracemalloc.start()
            self.smart_agent.choose_action(obs["observation"], action_mask=mask)
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"  Memory used : {peak / 10**6:.6f} MB")
            self.assertLess(peak / 10**6, 384, "The agent uses too mush memory (> 384MB)")

    def test_tournament(self):
        """
        Test the SmartAgent in a tournament setting against RandomAgent.
        """
        num_games = 100
        results, _ = play_multiple_games(num_games=num_games)

        smart_wins = results["smart_win"]
        random_wins = results["random_win"]

        self.assertGreaterEqual(smart_wins, random_wins, "SmartAgent should win more games than RandomAgent")
        self.assertGreaterEqual(smart_wins, 80, "SmartAgent should win 80% of the time against RandomAgent")


if __name__ == '__main__':
    unittest.main()

