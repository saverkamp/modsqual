from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='modsqual',
    version='0.5.0',
    py_modules=['modsqual'],
    description='An lxml wrapper for working with MODS XML data.',
    url='https://github.com/saverkamp/modsqual',
    author='Shawn Averkamp',
    author_email='shawnaverkamp@gmail.com',
    license='MIT',
    classifiers = [
    	'Programming Language :: Python :: 2.7',
    ],
    install_requires=['xmltodict'],
)
