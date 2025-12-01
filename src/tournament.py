# tournament.py
# Check if SmartAgent outperforms RandomAgent in multiple games of Connect Four

from pettingzoo.classic import connect_four_v3
from smart_agent import SmartAgent
from random_agent import RandomAgent
from tqdm import tqdm

def play_single_game(env, smart_agent, random_agent):
    """
    Play one full game between SmartAgent (red) and RandomAgent (yellow)

    Returns:
        +1 if SmartAgent wins
        -1 if RandomAgent wins
         0 for draw
    """

    env.reset()
    smart_name = env.agents[0]   # "player_0" (always first)
    random_name = env.agents[1]  # "player_1"

    while True:
        agent = env.agent_selection
        observation, reward, terminated, truncated, info = env.last()

        # Retrieve action mask
        action_mask = observation["action_mask"]

        # Choose action depending on which agent is playing
        if agent == smart_name:
            action = smart_agent.choose_action(
                observation["observation"],
                reward,
                terminated,
                truncated,
                info,
                action_mask=action_mask
            )
        else:
            action = random_agent.choose_action(
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
    smart_reward = rewards.get(smart_name, 0)
    random_reward = rewards.get(random_name, 0)

    if smart_reward > random_reward:
        return 1
    elif smart_reward < random_reward:
        return -1
    else:
        return 0


def run_tournament(n_games=100):
    """
    Runs n_games between SmartAgent and RandomAgent,
    alternating which agent goes first.
    """

    results = {"wins": 0, "losses": 0, "draws": 0}

    print(f"Running {n_games} games SmartAgent vs RandomAgent with alternated first player\n")

    for i in tqdm(range(n_games)):
        env = connect_four_v3.env()
        env.reset()
        smart_agent = SmartAgent(env)
        random_agent = RandomAgent(env)

        if i % 2 == 0:
            result = play_single_game(env, smart_agent, random_agent)
            if result == 1:
                results["wins"] += 1
            elif result == -1:
                results["losses"] += 1
            else:
                results["draws"] += 1
        else:
            result = play_single_game(env, random_agent, smart_agent)
            if result == 1:
                results["losses"] += 1  # player_0 (random) a gagné
            elif result == -1:
                results["wins"] += 1    # player_1 (smart) a gagné
            else:
                results["draws"] += 1
        

    print("\nTournament complete!")
    print(f"SmartAgent wins:   {results['wins']}")
    print(f"SmartAgent losses: {results['losses']}")
    print(f"Draws:             {results['draws']}")

    return results

if __name__ == "__main__":
    run_tournament(100)