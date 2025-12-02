# tournament.py
# Run tournaments between any two agents in Connect Four
from pettingzoo.classic import connect_four_v3
from tqdm import tqdm


def play_single_game(env, agent1_instance, agent2_instance):
    """
    Play one full game between two agents.
    
    Args:
        env: PettingZoo environment
        agent1_instance: First agent (player_0)
        agent2_instance: Second agent (player_1)
    
    Returns:
        +1 if agent1 wins
        -1 if agent2 wins
         0 for draw
    """
    env.reset()
    agent1_name = env.agents[0]  # "player_0"
    agent2_name = env.agents[1]  # "player_1"
    
    while True:
        agent = env.agent_selection
        observation, reward, terminated, truncated, info = env.last()
        
        # Retrieve action mask
        action_mask = observation["action_mask"]
        
        # Choose action depending on which agent is playing
        if agent == agent1_name:
            action = agent1_instance.choose_action(
                observation["observation"],
                reward,
                terminated,
                truncated,
                info,
                action_mask=action_mask
            )
        else:
            action = agent2_instance.choose_action(
                observation["observation"],
                reward,
                terminated,
                truncated,
                info,
                action_mask=action_mask
            )
        
        # If game is already finished
        if terminated or truncated:
            break
        
        env.step(action)
    
    # Final rewards
    rewards = env.rewards
    agent1_reward = rewards.get(agent1_name, 0)
    agent2_reward = rewards.get(agent2_name, 0)
    
    if agent1_reward > agent2_reward:
        return 1
    elif agent1_reward < agent2_reward:
        return -1
    else:
        return 0


def run_tournament(agents, n_games=100):
    """
    Runs n_games between two agents, alternating which agent goes first.
    
    Args:
        agents: List of two agent classes [AgentClass1, AgentClass2]
        n_games: Number of games to play (default: 100)
    
    Returns:
        Dictionary with wins/losses/draws for agent1
    """
    
    AgentClass1, AgentClass2 = agents
    agent1_name = AgentClass1.__name__
    agent2_name = AgentClass2.__name__
    
    results = {"wins": 0, "losses": 0, "draws": 0}
    
    print(f"\nRunning {n_games} games: {agent1_name} vs {agent2_name}")
    print(f"Alternating first player\n")
    
    for i in tqdm(range(n_games)):
        env = connect_four_v3.env()
        env.reset()
        
        agent1 = AgentClass1(env)
        agent2 = AgentClass2(env)
        
        if i % 2 == 0:
            # agent1 plays first (player_0)
            result = play_single_game(env, agent1, agent2)
            if result == 1:
                results["wins"] += 1
            elif result == -1:
                results["losses"] += 1
            else:
                results["draws"] += 1
        else:
            # agent2 plays first (player_0)
            result = play_single_game(env, agent2, agent1)
            if result == 1:
                results["losses"] += 1
            elif result == -1:
                results["wins"] += 1
            else:
                results["draws"] += 1
    
    print("\nTournament complete!")
    print(f"{agent1_name} wins:   {results['wins']}")
    print(f"{agent2_name} wins: {results['losses']}")
    print(f"Draws:             {results['draws']}")
    
    return results


if __name__ == "__main__":
    from smart_agent import SmartAgent
    from random_agent import RandomAgent
    from minimax_agent import MinimaxAgent
    
    #agents = [SmartAgent, RandomAgent]

    agents = [SmartAgent, MinimaxAgent]
    results = run_tournament(agents, 50)