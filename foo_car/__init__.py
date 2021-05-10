from gym.envs.registration import register

register(
    id='foo-ball-v0',
    entry_point='foo_car.envs:FooBall',
)
register(
    id='foo-vehicle-v0',
    entry_point='foo_car.envs:FooVehicle',
)

from foo_car.envs.foo_ball import FooBall
from foo_car.envs.foo_vehicle import FooVehicle