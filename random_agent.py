"""
My Random Agent for Connect Four

This agent chooses moves randomly from the available (valid) columns.
"""

import random


class RandomAgent:
    """
    A simple agent that plays randomly
    """

    def __init__(self, env, player_name=None):

        """
        Initialize the random agent

        Parameters:
            env: PettingZoo environment
            player_name: Optional name for the agent (for display)
        """
        
        self.env = env

        if not player_name :
            self.player_name = player_name 
        else : 
            self.player_name = "random_player"

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
        """
        Choose a random valid action

        Parameters:
            observation: numpy array (6, 7, 2) - current board state
            reward: float - reward from previous action
            terminated: bool - is the game over?
            truncated: bool - was the game truncated?
            info: dict - additional info
            action_mask: numpy array (7,) - which columns are valid (1) or full (0)

        Returns:
            action: int (0-6) - which column to play
        """
        # TODO: Implement random action selection
        action_space = self.env.action_space(self.env.agent_selection)
        
        action = action_space.sample(action_mask)

        return action


def choose_action_manual(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):
    """
    Choose a random valid action without using .sample()

    This is a learning exercise to understand what action_mask does
    """
    # TODO: Get list of valid actions from action_mask
    valid_actions = []  # Fill this list
    n=len(action_mask)
    for i in range (n): 
        if action_mask[i] == 1 : 
            valid_actions.append(i)

    # TODO: If no valid actions, return None (shouldn't happen in Connect Four)
    if not valid_actions:
        return None

    # TODO: Choose randomly from valid actions
    action = random.choice(valid_actions)
    return action # Replace with random choice
                
