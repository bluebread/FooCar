from foo_car.envs.foo_env import FooEnv, get_exe_file_path

class FooVehicle(FooEnv):
	def __init__(self, no_graphics:bool=False, seed:int=1, **config):
		file_name = get_exe_file_path('vehicle')
		super(FooVehicle, self).__init__(
			file_name,
			no_graphics=no_graphics,
			seed=seed,
			config=config
		)