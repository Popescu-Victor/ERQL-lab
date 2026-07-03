import gym
import numpy as np
import random



env = gym.make('Taxi-v3')

alpha = 0.8 # How much new actions affect the learned Q-values (learning rate)
gamma = 0.95 # Discount factor for future rewards
epsilon = 0.1 # Exploration rate for epsilon-greedy action selection
epsilon_decay = 0.99 # Decay rate for epsilon to reduce exploration over time
min_epsilon = 0.01 # Minimum exploration rate
num_episodes = 1000
max_steps_per_episode = 100