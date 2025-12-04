# test_suite.py

import unittest
import numpy as np
import random

import time
import tracemalloc

from pettingzoo.classic import connect_four_v3
from src.smart_agent import SmartAgent
from src.random_agent import RandomAgent
from Test.test_smart_vs_random import play_game_rvs, play_multiple_games_rvs

class TestConnectFour(unittest.TestCase):
    def setUp(self):
        """
        Initializes the agent by providing it with the required environment.
        """
        self.env = connect_four_v3.env()
        self.env.reset()
        self.agent = SmartAgent(self.env)


    def test_valid_action_bounds(self):
        """
        Test that the action chosen by the agent is within valid bounds (0-6).
        """
        observation, _, _, _, _ = self.env.last()
        obs = observation['observation']
        mask = observation['action_mask']
        
        action = self.agent.choose_action(obs, action_mask=mask)
        
        self.assertIn(action, range(7), "Action must be between 0 and 6")
        self.assertIsInstance(action, (int, np.integer), "Action must be an integer")

    def test_respect_action_mask(self):
        """
        Test that the agent respects the action mask and only chooses valid actions.
        """
        obs = np.zeros((6, 7, 2), dtype=np.int8)
        
        mask = np.array([0, 0, 0, 0, 0, 0, 1], dtype=np.int8)

        for col in range(6):
            obs[:, col, 0] = 1 # Fill columns 0-5 to make them invalid

        action = self.agent.choose_action(obs, action_mask=mask)
        
        self.assertEqual(action, 6, "Agent should choose the only valid action (column 6)")
        self.assertEqual(mask[action], 1, "Agent chose an invalid action according to the mask")

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
                
        obs[5, 0, 0] = 1 # place player 0 pieces
        obs[4, 0, 0] = 1
        obs[3, 0, 0] = 1

        obs[5, 1, 1] = 1 # place opponent's pieces
        obs[4, 1, 1]= 1
        obs[3, 1, 1]= 1

        mask = np.ones(7, dtype=np.int8) # all actions valid
        action = self.agent.choose_action(obs, action_mask=mask)
        self.assertEqual(action, 0, "Agent should play col 0 to block opponent")

class TestPerformanceAndTournament(unittest.TestCase):
    def setUp(self):
        """
        Initializes the environment and agents for performance and tournament tests.
        """
        self.env = connect_four_v3.env()
        self.env.reset()
        self.smart_agent = SmartAgent(self.env)
        self.random_agent = RandomAgent(self.env)

    def test_speed(self):
        """
        Test the performance of the SmartAgent in terms of execution time.
        """

        self.env.reset()
        observation, _, _, _, _ = self.env.last()
        obs = observation["observation"]
        mask = observation["action_mask"]

        start_time = time.time()
        iter = 100
        for _ in range(iter):
            self.smart_agent.choose_action(obs, action_mask=mask)
        
        end_time = time.time()
        avg_time = (end_time - start_time) / 100
        
        print(f"  Average action time : {avg_time:.6f} seconds")
        self.assertLess(avg_time, 3, "The agent is too slow (> 3s per action)")
        
    def test_memory(self):
            """
            Test the performance of the SmartAgent in terms of memory.
            """
            self.env.reset()
            observation, _, _, _, _ = self.env.last()
            obs = observation["observation"]
            mask = observation["action_mask"]            
            tracemalloc.start()
            self.smart_agent.choose_action(obs, action_mask=mask)
            _, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()

            print(f"  Memory used : {peak / 10**6:.6f} MB")
            self.assertLess(peak / 10**6, 384, "The agent uses too mush memory (> 384MB)")

    def test_tournament(self):
        """
        Test the SmartAgent in a tournament setting against RandomAgent.
        """
        num_games = 100
        results, _, _ = play_multiple_games_rvs(num_games=num_games)

        smart_wins = results["smart_win"]
        random_wins = results["random_win"]

        self.assertGreaterEqual(smart_wins, random_wins, "SmartAgent should win more games than RandomAgent")
        self.assertGreaterEqual(smart_wins, 80, "SmartAgent should win 80% of the time against RandomAgent")
