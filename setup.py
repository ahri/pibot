from setuptools import setup, find_packages

setup(
    name='pibot',
    version='0.1',
    packages=find_packages(),  # have a look at the docs, it basically includes all the packages in the current directory
    url='http://www.example.com',
    license='Apache 2.0',
    author='Mike Piper',
    author_email='mike.piper@gmail.com',
    description='',
    install_requires=[],
    tests_require=[
        'PyHamcrest==1.7.1',
        'doublex==1.6.1'
    ],
    test_suite='tests.test_all',
    package_data={'': ['README.rst']},
)
