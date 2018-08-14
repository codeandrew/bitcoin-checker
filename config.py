#!/usr/bin/env python
import os 
#print os.environ

pwd = os.getenv('TOOLS', os.getcwd() )  

def list():
	for item, value in os.environ.items():
	    print('{}: {}'.format(item, value))

	for i, j in os.environ.items():
	    print(i, j)


def execute():
	env = open( pwd + "/.env", "r")

	print env.read()
	print type(env.read())

execute()

