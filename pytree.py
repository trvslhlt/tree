#!/usr/bin/env python3
import os
import subprocess
import sys


# YOUR CODE GOES here

# determine number of inputs
def validateInputs():
    inputCount = len(sys.argv)
    if inputCount == 1:
        return # no argument passed
    elif inputCount == 2:
        currentDirectoryPath = os.path.dirname(os.path.abspath(__file__))
        argumentPath = os.path.join(currentDirectoryPath, sys.argv[1])
        if os.path.isdir(argumentPath):
            return
        else:
            print('please pass in a valid directory to tree')
            sys.exit(1)
    else:
        print('please pass in 0 or 1 arguments')
        sys.exit(1)

def findTreeRoot():
    inputCount = len(sys.argv)
    currentDirectoryPath = os.path.dirname(os.path.abspath(__file__))
    if inputCount == 1:
        return currentDirectoryPath
    else:
        return os.path.join(currentDirectoryPath, sys.argv[1])


def run():
    validateInputs()
    rootDirectory = findTreeRoot()
    print(rootDirectory)

if __name__ == '__main__':
    # just for demo
    #subprocess.run(['tree'] + sys.argv[1:])
    run() 
