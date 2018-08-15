#!/usr/bin/env python
import os

cwd = os.getenv('TOOLS', os.getcwd())

def list():
    for item, value in os.environ.items():
        print('{}: {}'.format(item, value))

    for i, j in os.environ.items():
        print(i, j)


def execute():
    env = open( cwd + "/.env", "r")

    print env.read()

if __name__ == '__main__':
    print "Main file is config.py"
    execute()

