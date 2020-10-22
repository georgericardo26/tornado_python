import cmd
from distutils import command

from setuptools import setup, find_packages

requires = [
    'tornado',
    'tornado-sqlalchemy',
    'psycopg2-binary',
]

setup(
    name='app_name',
    version='0.0',
    description='A app created by me',
    author='George Ricardo',
    author_email='georgericardo26@gmail.com',
    keywords='web tornado',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'start_app = core.settings:main',
        ],
    },
)
