from setuptools import setup, find_packages

setup(
    name='pt_pump_up',
    version='2.2.3',
    description='Hub for Portuguese NLP resources',
    install_requires=['beanie', 'mechanize',
                      'pandas', 'requests', 'scikit-learn', 'numpy'],
    packages=find_packages(),
    author='Rúben Almeida'
)
