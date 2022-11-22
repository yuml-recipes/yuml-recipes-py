from setuptools import find_packages, setup

setup(
    name='yumlrecipes',
    packages=find_packages(include=['yuml']),
    version='0.1.0',
    description='Yuml Recipes Python Library',
    author='Patrick Eschenbach',
    license='GPL-3.0',
    install_requires=['pyyaml'],
)
