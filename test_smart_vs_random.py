from pettingzoo.classic import connect_four_v3
import numpy as np
import src.random_agent as ra
import src.smart_agent as sa 


def play_game_rvs(player_0=False): 
    """
    Play a game using RandomAgent for one player and SmartAgent for the other

    arguments : 
        player_0 : bool, if True, player_0 is smart 
                        else, player_1 is smat

    returns : the result of the game
    """

    env = connect_four_v3.env(render_mode=None) # ou render_mode="rdb_array" ou bien None
    env.reset(seed=42)

    count = 0 # counts number of steps
    agents = {} # random agents
    outcome = None # outcome of the game : which player won or draw

    for agent_name in env.agents:
        if (agent_name == "player_0" and player_0) or \
           (agent_name == "player_1" and not player_0):
            agents[agent_name] = sa.SmartAgent(env) 
        else:
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
            a = agents[agent]
            action = a.choose_action(observation["observation"], reward, termination, truncation, info, observation["action_mask"])

        env.step(action)
        count += 1

    env.close()
    #print(f"Game finished in {count} steps.")

    smart_agent_name = "player_0" if player_0 else "player_1"

    return outcome, count, smart_agent_name



def play_multiple_games(num_games=10):
    """
    Play multiple games to test SmartAgent against RandomAgent

    Arguments : 
        num_games : int, number of games that will be played 

    Returns : the result of the game
    """

    actions = []
    results = {"smart_win":0, "random_win":0, "draw":0}

    print(f"\nLet's start the game in {num_games} rounds")

    for i in range (num_games): 
        player_0 = (i%2 == 0)

        outcome, count, smart_agent_name = play_game_rvs(player_0)

        if outcome == "draw" : 
            results["draw"] +=1
        elif outcome == smart_agent_name:
            results["smart_win"] +=1
        else : 
            results["random_win"] +=1

        actions.append(count)
        #print(f"Game {i+1} results: {results}")

    return results, actions


results, actions = play_multiple_games(100)

print(f"Game results: {results}")
average = np.mean(actions)
min = np.min(actions)
max = np.max(actions)
print(f"Average action : {average}, minimum actions : {min}, maximum actions : {max}")







