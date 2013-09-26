#!/usr/bin/env python
from __future__ import print_function
from setuptools import setup
import codecs
import subprocess as subp
import sys


appname = 'bgtunnel'
version = __import__(appname).__version__


read = lambda filepath: codecs.open(filepath, 'r', 'utf-8').read()


if sys.argv[-1] == 'publish':
    subp.check_output(('python', 'setup.py', 'sdist', 'upload'))
    # Git tagging. Yes I'm lazy!
    if version not in subp.check_output(('git', 'tag', '-l', version)):
        subp.check_output(('git', 'tag', '-a', version,
                           '-m', 'Version {0}'.format(version)))
        subp.check_output(('git', 'push', '--tags'))
    sys.exit()

setup(
    name=appname,
    version=version,
    description="Initiate SSH tunnels in the background",
    long_description=read(os.path.join(os.path.dirname(__file__),
                                       'README.md')),
    py_modules=[appname],
    author='Jacob Magnusson',
    author_email='m@jacobian.se',
    url='https://github.com/jmagnusson/bgtunnel',
    license='BSD',
    platforms=['unix', 'macos'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)