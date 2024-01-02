from setuptools import setup, find_packages

setup(
    name='pt_pump_up_admin',
    version='0.0.2',
    description='Administrative tools to interact with PT-Pump-Up Platform',
    install_requires=[
        'requests',
        'mechanize',
        'pandas',
        'scikit-learn',
        'numpy',
        'huggingface_hub',
        'mechanize',
        'nltk',
        'tqdm',
    ],
    packages=find_packages(),
    author='Rúben Almeida'
)
