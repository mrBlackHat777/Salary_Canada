import pathlib
from setuptools import setup, find_packages

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
readme = pathlib.Path('README.md').read_text()

setup(
    author='AlgoÉTS',
    name='Template-Strategy',
    description='Template-Strategy is a Jupyter and Python Project designed to help with the development of algorithmic trading strategies.',
    long_description=readme,
    long_description_content_type='text/markdown',
    version='0.0.1',
    license='Apache 2.0',
    python_requires='>=3.7',
    url='https://github.com/AlgoETS/Template-Strategy',
    package_dir={'': 'code'},
    packages=find_packages(where='code'),
    include_package_data=True,
    install_requires=requirements
)

