from gym.envs.registration import register

register(
    id='foo-v0',
    entry_point='gym_foo.envs:FooCarEnv',
)

from foo_car.envs.foo_env import FooCarEnv