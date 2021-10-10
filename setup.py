from os.path import dirname, join

from setuptools import setup

setup(
    name='logexdec',
    version='0.0.2',
    license='MIT',
    author='Evgeniy Burdin',
    author_email='e.s.burdin@gmail.com',
    packages=['logexdec'],
    description='Decorator for logging exceptions in functions and methods.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type="text/markdown",
    url='https://github.com/EvgeniyBurdin/logexdec',
    keywords='decorator function method logging logger exception',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
    ],
    python_requires='>=3.7',
)