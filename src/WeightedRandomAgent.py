import random


class WeightedRandomAgent(RandomAgent):
    """
    Random agent that prefers center columns
    """

    def choose_action(self, observation, reward=0.0, terminated=False, truncated=False, info=None, action_mask=None):

        n = len(action_mask)
        valid_actions = [] 
        for i in range (n) : 
            if action_mask[i] == 1 :
                valid_actions.append(i)
        
        if not valid_actions : 
            return None 

        
        
        # TODO: Create weights that favor center (column 3)
        # TODO: Filter by action_mask
        # TODO: Use random.choices(actions, weights=weights)
        pass

