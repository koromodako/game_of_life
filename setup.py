from pathlib import Path
from setuptools import setup, find_packages
from game_of_life import __version__

HERE = Path(__file__).absolute().parent
CONF_DIR = Path.home().joinpath('.config')

def requirements():
    with HERE.joinpath('requirements.txt').open() as reqs:
        return list([req.strip() for req in reqs if req.strip()])

setup(
    # main information
    name='game_of_life',
    version=__version__,
    description='',
    author='Koromodako',
    author_email='koromodako@gmail.com',
    url='https://github.com/koromodako/game_of_life',
    # package files
    packages=find_packages(str(HERE)),
    install_requires=requirements(),
    # configuration files
    entry_points={
        'console_scripts': [
            'gol = game_of_life.main:main',
        ]
    },
#    data_files=[(str(CONF_DIR), ['game_of_life.yml'])]
)
