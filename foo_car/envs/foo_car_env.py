import math
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union

import gym
from gym import spaces, logger
import numpy as np

from gym_unity.envs import UnityToGymWrapper
from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.base_env import ActionTuple
from mlagents_envs.side_channel.environment_parameters_channel import EnvironmentParametersChannel

file_path = Path(__file__)
UNITY_ENV_EXE_FILE = str(file_path.parents[1].joinpath('unity_env', 'FooCar.exe'))

class FooCarEnv(gym.Env):
	_channel = EnvironmentParametersChannel()

	PathSpace = {
		'xyz': 0,
		'xy': 1,
		'xz': 2
	}

	def __init__(self, no_graphics:bool=False, seed:int=1, **config):
		self._config = config
		self._unity_env = UnityEnvironment(
			file_name=UNITY_ENV_EXE_FILE,  
			no_graphics=no_graphics,
			seed=seed, 
			side_channels=[self._channel]
		)
		for key, value in config.items():
			self._channel.set_float_parameter(key, float(value))
		
		self._gym_env = UnityToGymWrapper(self._unity_env)

	def step(self, action):
		obs, reward, done, info = self._gym_env.step(action)
		size = self.observation_size

		return obs[:size], reward, done, info

	def reset(self):
		obs = self._gym_env.reset()
		size = self.observation_size
		return obs[:size]

	def render(self, mode="rgb_array"):
		return self._gym_env.render(mode=mode)
	
	def seed(self, seed=None):
		self._gym_env.seed(seed=seed) # it will throw a warning

	def close(self):
		self._gym_env.close()

	@property
	def metadata(self):
		return self._gym_env.metadata

	@property
	def reward_range(self) -> Tuple[float, float]:
		return self._gym_env.reward_range

	@property
	def action_space(self):
		return self._gym_env.action_space

	@property
	def observation_space(self):
		return self._observation_space
		
	@property
	def observation_size(self):
		# Reference: readonly variable (Unity)FooCar/CarAgent.ObservationSize
		config = self._config
		space = self.PathSpace

		path_space = config['path_space'] if 'path_space' in config else space['xz']
		ticker_end = config['ticker_end'] if 'ticker_end' in config else 5
		ticker_start = config['ticker_start'] if 'ticker_start' in config else -3

		xyz_mode = (path_space == space['xyz'])
		basic_num = 3 + (3 if xyz_mode else 2)
		point_dim = 6 if xyz_mode else 4

		return basic_num + point_dim * (ticker_end - ticker_start + 1)

