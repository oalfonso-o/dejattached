import os
from setuptools import find_packages, setup
from dejavu import __version__

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'Django',
    'django-jet',
    'django-filter',
    'djangorestframework',
    'django-cors-headers',
    'python-dotenv',
    'bcrypt',
    'coreapi',
    'Markdown',
    'pygments',
    'pyyaml',
],

setup(
    name='oalfonso-dejavu',
    version=__version__,
    packages=find_packages(),
    license='MIT',
    description='Dejavu Oalfonso',
    long_description=README,
    url='https://bitbucket.org/oalfonso_o/',
    author='Oriol Alfonso',
    author_email='oriolalfonso91@gmail.com',
    install_requires=install_requires,
    package_data={'oalfonso': ['fixtures/*']},
)
