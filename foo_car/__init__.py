from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='foo_car.envs:FooCarEnv',
)

from foo_car.envs.foo_car_env import FooCarEnv