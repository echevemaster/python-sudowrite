#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014 echevemaster.org
# Eduardo Echeverria - <echevemaster@gmail.com>

'''sudowrite

Usage:
  sudowrite useradd <user>
  sudowrite userdel <user>
  sudowrite --version
  sudowrite -h | --help

Options:
  -h --help           Show this screen.
  --version           Show version.
'''

from __future__ import unicode_literals, print_function
import os
from docopt import docopt
from functools import wraps
from status_codes import _status_codes as _msg

__version__ = '0.1.0'
__author__ = 'Eduardo Echeverria'
__license__ = 'BSD'


def useradd(args):
    '''
    Add an user to sudoers file
    '''
    username = args.get('<user>')
    cmd = username + '  ALL=(ALL)   ALL\n'
    if username:
        with open('sudoers', 'a') as f:
            f.write(cmd)
        print(_msg.get(300))


def main():
    ''' Main entry point for sudowrite cli.'''
    args = docopt(__doc__, version=__version__)
    if args.get('useradd'):
        useradd(args)

# Execute the application
if __name__ == '__main__':
    main()
