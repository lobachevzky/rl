from setuptools import setup, find_packages

setup(name='rl',
      packages=find_packages(),
      install_requires=[
          'tensorflow',
          'gym',
          'gym[atari]',
          'pygame',
      ])