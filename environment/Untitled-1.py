# %%
"""
Runs an example with 2 agents in the pvpbox env
Adapted from https://github.com/minerllabs/minerl/blob/dev/tests/multiagent_test.py
"""

__author__ = "Sander Schulhoff"
__email__ = "sanderschulhoff@gmail.com"
import sys
sys.path.append("..")
# from minerl.env.malmo import InstanceManager
import argparse
from pvpbox_specs import PvpBoxNoQuit
from wrappers import OneVersusOneWrapper
import gym
import random
env_spec = PvpBoxNoQuit(agent_count=2)

#     # IF you want to use existing instances use this!
#     # instances = [
#     #     InstanceManager.add_existing_instance(9001),
#     #     InstanceManager.add_existing_instance(9002)]
instances = []
agent_actions = [("attack", 1), ("left", 1), ("right", 1), ("camera", [0,15]), ("camera", [0,-15])]

env = OneVersusOneWrapper(env_spec.make(instances=instances), agent_actions)

for i in range(10):
    obs = env.reset()
    print(obs)
    steps = 0

    done = {"__all__":False}
    while not done["__all__"]:
        steps += 1
        env.env.render()
        actions = {
            "agent_0": random.choice(range(0,5)),
            "agent_1": random.choice(range(0,5))
        }
        # actions = env.action_space.sample()

        # print(str(steps) + " actions: " + str(actions))
        print(done)
        obs, reward, done, info = env.step(actions)
        print(done)
    


