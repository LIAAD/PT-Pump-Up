from setuptools import setup, find_packages

setup(
    name='pt_pump_up',
    version='2.1.3',
    description='Hub for Portuguese NLP resources',
    install_requires=['beanie', 'mechanize'],
    packages=find_packages(),
    author='Rúben Almeida'
)
