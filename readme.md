# Foo Car

Installation:

	$ git clone https://github.com/bluebread/FooCar.git
    $ pip install -e FooCar

How to get the enviroment:

```python
import gym
env = gym.make('foo_car:foo-v0')
```

Example:

```python
import gym

config = {
    'num_anchors': 20,
    'radius_anchor_circle': 16,
    'radius_epsilon_ratio': 0.5,
    'theta_epsilon_ratio':  0.5,
    'max_anchor_height': 2.0,
    'max_anchor_angle': 0.0,
    'road_width': 1.2,
    'agent_mass': 1.5,
    'force_multiplier': 12,
    'ticker_start': -4,                			
    'ticker_end': 6,
    'ticker_space': 0.3,
    'running_penalty': -10.0,
    'failure_penalty': -150.0,
}

env = gym.make('foo_car:foo-ball-v0', no_graphics=False, **config)
obs = env.reset()
for i in range(100):
	env.render()
	action = env.action_space.sample()
	obs, reward, done, info = env.step(action)
	if done:
		break
env.close()
```

## NOTE

1. In Linux platform without GUI, 'no_graphics' (one of parameters of gym.make) MUST be 'True'.
2. In Vehicle enviroment, Friction & WindForce accidents DO NOT work at all. That is, 'LossControl' accident is the only accident that will affect the moving of the agent. 