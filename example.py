import os
import time

import gym

from foo_car.envs.foo_car_env import FooCarEnv

def common_testcase():
	config = {
		# 'enableFrictionAccident': True,     # default false
		# 'frictionchanged_time': 1.0,      # default 3.0
		# 'static_friction': 0.8,           # default 0.0
		# 'dynamic_friction': 0.4,          # default 0.0
		
		'enableWindAccident': True,         # default false
		'wind_time': 6,                 # default 3.0
		'wind_force_X': 2.0,              # default 0.0
		'wind_force_Y': 3.1,              # default 0.0, only for 3d path
		'wind_force_Z': 1.5,              # default 0.0

		# 'enableLossControlAccident': True,  # default false
		# 'lossctrl_time': 1.0,             # default 3.0
		# 'lossctrl_Xaxis_ratio': 0.7,      # default 1.0
		# 'lossctrl_Zaxis_ratio': 0.3,      # default 1.0
	}
	env = gym.make('foo_car:foo-v0', no_graphics=False, **config)

	for i_e in range(3):
		obs = env.reset()
		print(0)
		print("\tobs:", obs)
		for i in range(250):
			env.render()
			action = env.action_space.sample()
			obs, reward, done, info = env.step([0.0, 0.0])
			print("%d-%d:" % (i_e, i))
			print("\taction:", action)
			print("\tobs:", obs)
			print("\treward:", reward)
			print("\tdone:", done)
			if done:
				print("Episode finished after {} timesteps".format(i+1))
				break
	env.close()

def parameters_testcase(config:dict):
	env = gym.make('foo_car:foo-v0', no_graphics=False, **config)

	obs = env.reset()
	print(0)
	print("\tobs:", obs)
	for i in range(10):
		env.render()
		action = env.action_space.sample()
		obs, reward, done, info = env.step(action)
		print("%d:" % i)
		print("\tobs:", obs)
		print("\treward:", reward)
		if done:
			break
	env.close()

config = {
    # 'num_anchors': 20,                 # default 10
    # 'radius_anchor_circle': 16,      # default 8.0
    # 'radius_epsilon_ratio': 0.5,      # default 0.7
    # 'theta_epsilon_ratio':  0.5,      # default 0.7
    # 'max_anchor_height': 2.0,         # default 1.0, only for 3d path
    # 'max_anchor_angle': 0.0,          # default 15.0, only for 3d path
    # 'path_space': FooCarEnv.PathSpace['xyz'],            # default PathSpace.xz
    # 'road_width': 1.2,                # default 1.0
    # 'agent_mass': 1.5,                # default 1.0
    # 'force_multiplier': 12,          # default 10
    # 'ticker_start': -4,                # default -3
    # 'ticker_end': 6,                  # default 5
    # 'ticker_space': 0.3,              # default 0.2
    # 'running_penalty': -10.0,           # default -5.0
    # 'failure_penalty': -150.0,           # default -100.0

    # 'enableFrictionAccident': True,     # default false
    # 'frictionchanged_time': 0.1,      # default 3.0
    # 'static_friction': 0.8,           # default 0.0
    # 'dynamic_friction': 0.4,          # default 0.0
	
    # 'enableWindAccident': True,         # default false
    # 'wind_time': 0.1,                 # default 3.0
    # 'wind_force_X': 2.0,              # default 0.0
    # 'wind_force_Y': 3.1,              # default 0.0, only for 3d path
    # 'wind_force_Z': 1.5,              # default 0.0

    'enableLossControlAccident': True,  # default false
    'lossctrl_time': 1.0,             # default 3.0
    'lossctrl_Xaxis_ratio': 0.7,      # default 1.0
    'lossctrl_Zaxis_ratio': 0.3,      # default 1.0
}

if __name__ == '__main__':
	# common_testcase()
	parameters_testcase(config)
	pass