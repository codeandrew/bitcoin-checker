#!/usr/bin/env python
import os

SENDER_EMAIL = SENDER_EMAIL
RECEIVER_EMAIL = RECEIVER_EMAIL
PASSWOR = PASSWORD

cwd = os.getenv('TOOLS', os.getcwd())

def list():
    for item, value in os.environ.items():
        print('{}: {}'.format(item, value))

    for i, j in os.environ.items():
        print(i, j)


def execute():
    env = open( cwd + "/.env", "r")

    print env.read()

execute()

