import os
import time

import gym

from foo_car.envs.foo_env import FooEnv
import time


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
	config['worker_id'] = 1
	env = gym.make('foo_car:foo-ball-v0', no_graphics=True, **config)
	config['worker_id'] = 2
	env2 = gym.make('foo_car:foo-ball-v0', no_graphics=True, **config)

	# env = gym.make('Hopper-v2')
	current_time = time.time()
	start_time = current_time
	origin_time = time.time()
	total_count = 0
	for i_e in range(100):
		# start_time = time.time()
		obs = env.reset()
		print(0)
		print("\tobs:", obs)
		for i in range(100):
			current_time = time.time()
			time_interval = current_time - start_time
			total_time = current_time - origin_time
			start_time =  current_time
			print(f'time interval: {time_interval}, fps: {1 / time_interval}, till now: {total_time}, aver. fps: {total_count / total_time}')
			total_count += 1
			# env.render()
			action = env.action_space.sample()
			obs, reward, done, info = env.step(action)
			print("%d-%d:" % (i_e, i))
			print("\taction:", action)
			print("\tobs:", obs)
			print("\treward:", reward)
			print("\tdone:", done)
			if done:
				print("Episode finished after {} timesteps".format(i+1))
				break
		cur_time = time.time()
		print('fps: %f' % (100 / (cur_time - start_time)))

	env.close()

def parameters_testcase(config:dict):
	env = gym.make('foo_car:foo-ball-v0', no_graphics=False, **config)
	# env = gym.make('foo_car:foo-vehicle-v0', no_graphics=False, **config)

	for i_e in range(3):
		print(i_e)
		obs = env.reset()
		# print(0)
		# print("\tobs:", obs)
		for i in range(10000):
			env.render()
			action = env.action_space.sample()
			obs, reward, done, info = env.step([0,1])
			print("%d:" % i)
			# print("\tobs:", obs)
			print("\treward:", reward)
			if done:
				break
	env.close()

config = {
    'num_anchors': 10,                 # default 10
    'radius_anchor_circle': 8,      # default 40.0
    'radius_epsilon_ratio': 0.5,      # default 0.4
    'theta_epsilon_ratio':  0.5,      # default 0.4
    # 'max_anchor_height': 2.0,         # default 3.0, only for 3d path
    # 'max_anchor_angle': 0.0,          # default 15.0, only for 3d path
    # 'path_space': FooCarEnv.PathSpace['xyz'],            # default PathSpace.xz
    'road_width': 1.0,                # default 5.0
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

    # 'enableLossControlAccident': True,  # default false
    # 'lossctrl_time': 1.0,             # default 3.0
    # 'lossctrl_Xaxis_ratio': 0.7,      # default 1.0
    # 'lossctrl_Zaxis_ratio': 0.3,      # default 1.0
}

if __name__ == '__main__':
	# common_testcase()
	parameters_testcase(config)
	pass