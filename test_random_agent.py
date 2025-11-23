# trest_random_agent.py
# type: ignore[reportMissingImports]

from pettingzoo.classic import connect_four_v3
import random_agent as ra

env = connect_four_v3.env(render_mode="human") # ou render_mode="rdb_array" ou bien None
env.reset(seed=42)

count = 0
# create a random agents
agents = {}

for agent_name in env.agents:
    agents[agent_name] = ra.RandomAgent(env)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
        if reward == 1:
            print(f"{agent} wins!")
        elif reward == 0:
            print("It's a draw!")
    else:
        # Take a random valid action
        mask = observation["action_mask"]
        action = env.action_space(agent).sample(mask)
        print(f"{agent} plays column {action}")

    env.step(action)
    count += 1

env.close()
print(f"Game finished in {count} steps.")