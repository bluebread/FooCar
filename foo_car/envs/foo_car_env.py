import math
from pathlib import Path
from typing import Any, Dict, List, Tuple, Union
from sys import platform
import os

import gym
from gym import spaces, logger
import numpy as np

from gym_unity.envs import UnityToGymWrapper
from mlagents_envs.environment import UnityEnvironment
from mlagents_envs.base_env import ActionTuple
from mlagents_envs.side_channel.environment_parameters_channel import EnvironmentParametersChannel

UNITY_ENV_EXE_FILE = ''
FILE_PATH = Path(__file__)
UNITY_ENV_EXE_FILE = str(FILE_PATH.parents[1].joinpath('unity_env', platform, 'FooCar'))

if platform not in ['win32', 'linux', 'darwin']:
	print("FooCar: Platform (%s) is not supported." % (platform))
	quit() # Abort

if platform == 'linux':
	os.system("chmod -R 755 %s.x86_64" % (UNITY_ENV_EXE_FILE))

class FooCarEnv(gym.Env):
	_channel = EnvironmentParametersChannel()

	PathSpace = {
		'xyz': 0,
		'xy': 2,
		'yz': 2,
		'xz': 2
	}

	def __init__(self, no_graphics:bool=False, seed:int=1, **config):
		self._config = config
		worker_id = 0
		if 'worker_id' in config:
			worker_id = config['worker_id']
		self._unity_env = UnityEnvironment(
			file_name=UNITY_ENV_EXE_FILE,
			# file_name=None, # Unity Editor Mode (debug)
			no_graphics=no_graphics,
			seed=seed, 
			side_channels=[self._channel],
			worker_id=worker_id
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
		config = self._config
		space = self.PathSpace

		path_space = config['path_space'] if 'path_space' in config else space['xz']
		r = config['radius_anchor_circle'] if 'radius_anchor_circle' in config else 8.0
		r_e = config['radius_epsilon_ratio'] if 'radius_epsilon_ratio' in config else 0.7
		h = config['max_anchor_height'] if 'max_anchor_height' in config else 1.0

		xyz_mode = (path_space == space['xyz'])
		bound = max(r * (1 + r_e), h if xyz_mode else 0)
		shape = (self.observation_size,)
		
		return gym.spaces.Box(-bound, +bound, dtype=np.float32, shape=shape)
		
	@property
	def observation_size(self):
		# Reference: readonly variable (Unity)FooCar/CarAgent.ObservationSize
		config = self._config
		space = self.PathSpace

		path_space = config['path_space'] if 'path_space' in config else space['xz']
		ticker_end = config['ticker_end'] if 'ticker_end' in config else 5
		ticker_start = config['ticker_start'] if 'ticker_start' in config else -3

		xyz_mode = (path_space == space['xyz'])
		basic_num = 6
		point_dim = 3 if xyz_mode else 2

		return basic_num + 2 * point_dim * (ticker_end - ticker_start + 1)
