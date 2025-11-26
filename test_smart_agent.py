# test_smart_agent.py

from smart_agent import SmartAgent

def test_get_valid_actions(self):
    agent = SmartAgent(env)
    mask = [1, 1, 1, 1, 1, 1, 1]  # All columns valid
    assert agent._get_valid_actions(mask) == [0, 1, 2, 3, 4, 5, 6]

    mask = [0, 1, 0, 1, 0, 1, 0]  # Only odd columns
    assert agent._get_valid_actions(mask) == [1, 3, 5]