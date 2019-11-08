#!/usr/bin/python3
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Api encurtar url'
__long_description__ = 'Esta api server para encurtar url'

__author__ = 'Romario Vargas'
__author_email__ = 'romario.getulio@gmail.com'

testing_extras = [
    'pytest',
    'pytest-cov',
]

setup(
    name='api',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='Linx',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/romario1990/flask-api-url.git',
    keywords='API, MongoDB',
    include_package_data=True,
    zip_safe=False,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    extras_require={
        'testing': testing_extras,
    },
)