from setuptools import setup

setup(name='foo_car',
      version='0.0.1',
      install_requires=[
		  'gym',
		  'gym_unity',
		  'numpy',
		  'mlagents; python_version >= "0.25.0"'
	  ]  # And any other dependencies foo needs
)