#!/usr/bin/env python
# flake8: noqa
from setuptools import find_packages, setup

setup(
    name='waveshare-epd',
    description='Waveshare e-Paper Display',
    author='Waveshare',
    package_dir={'': 'lib'},
    packages=['waveshare_epd'],
    install_requires=['w1thermsensor==1.3.0']
)
