# test_random_agent.py
# type: ignore[reportMissingImports]

from pettingzoo.classic import connect_four_v3
import random_agent as ra

def play_game():
    """
    Play a game using RandomAgent for both players

    Returns : the result of the game
    """
    env = connect_four_v3.env(render_mode="human") # ou render_mode="rdb_array" ou bien None
    env.reset(seed=42)

    count = 0 # counts number of steps
    agents = {} # create a random agents
    outcome = None # outcome of the game : which player won or draw

    for agent_name in env.agents: # initialize RandomAgents
        agents[agent_name] = ra.RandomAgent(env)

    for agent in env.agent_iter():
        observation, reward, termination, truncation, info = env.last()

        if termination or truncation:
            action = None
            if reward == 1:
                outcome = agent
                #print(f"{agent} wins!")
            elif reward == 0:
                outcome = "draw"
                #print("It's a draw!")
        else:
            # Take a random valid action
            a = agents[agent]
            action = a.choose_action(observation, reward, termination, truncation, info, observation["action_mask"])

        env.step(action)
        count += 1

    env.close()
    print(f"Game finished in {count} steps.")

    return outcome

def play_multiple_games(num_games=10):
    """
    Play multiple games to test RandomAgent
    """
    results = {"player_0": 0, "player_1": 0, "draws": 0}
    print(f"\nLet's start the game in {num_games} rounds")
    for i in range(num_games):
        print(f"\nStarting game {i+1}")
        outcome = play_game()
        results[outcome] += 1
        print(f"Game {i+1} results: {results}")

    return results

### Test the RandomAgent by playing multiple games ##
play_multiple_games(2)