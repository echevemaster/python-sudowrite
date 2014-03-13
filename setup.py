# Copyright (c) 2014 Eduardo Echeverria
# Eduardo Echeverria - <echevemaster@gmail.com>
import sys
import os
import subprocess

from setuptools import setup

PUBLISH_CMD = 'python setup.py register sdist upload'
TEST_PUBLISH_CMD = 'python setup.py register -r test sdist upload -r test'

if 'publish' in sys.argv:
    status = subprocess.call(PUBLISH_CMD, shell=True)
    sys.exit(status)

if 'publish_test' in sys.argv:
    status = subprocess.call(TEST_PUBLISH_CMD, shell=True)
    sys.exit()


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name='python-sudowrite',
    version='0.1.0',
    description='A python script for manage sudoers file'
    long_description=read('README.rst'),
    author='Eduardo Echeverria',
    author_email='echevemaster@gmail.com | echevemaster@fedoraproject.org',
    url='https://github.com/echevemaster/python-sudowrite',
    install_requires=['docopt'],
    license=read('LICENSE'),
    zip_safe=False,
    keywords='sudoers, sudo, roles',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'sudowrite = sudowrite:main'
        ]
    }
)
