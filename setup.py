#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
    name='pibot',
    version='0.1-dev',
    packages=find_packages(),
    author='Mike Piper',
    author_email='mike.piper@gmail.com',
    description='',
    install_requires=[],
    tests_require=[
        'PyHamcrest==1.7.1',
        'doublex==1.6.1'
    ],
    test_suite='tests.test_all',
)
