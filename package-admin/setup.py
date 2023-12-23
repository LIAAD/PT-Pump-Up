from setuptools import setup, find_packages

setup(
    name='pt_pump_up_admin',
    version='0.0.1',
    description='Administrative tools to interact with PT-Pump-Up Platform',
    install_requires=['requests'],
    packages=find_packages(),
    author='Rúben Almeida'
)