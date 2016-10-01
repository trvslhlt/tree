#!/usr/bin/env python3
import os
import subprocess
import sys


# YOUR CODE GOES here

# determine number of inputs
def validateInputs():
    '''
    validates the script's arguments. exits with error for invalid inputs
    '''
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
    '''
    returns the tree's root directory
    '''
    inputCount = len(sys.argv)
    currentDirectoryPath = os.path.dirname(os.path.abspath(__file__))
    if inputCount == 1:
        return currentDirectoryPath
    else:
        return os.path.join(currentDirectoryPath, sys.argv[1])


def buildTree(rootDirectory):
    
    def internalBuildTree(directory, level, lineHead, tree):
        names = os.listdir(directory)
        for idx, name in enumerate(names):
            if name.startswith('.'):
                continue
            namepath = os.path.join(directory, name)
            hatPipe = 'f'
            if idx ==  len(names) - 1:
                hatPipe = 'L'
            tree =  tree + '\n' + lineHead +  hatPipe + '-- ' + name
            if os.path.isdir(namepath):
                descender = "   " if idx == (len(names) - 1) else "|  "
                tree = internalBuildTree(namepath, level + 1, lineHead + descender, tree)
        return tree
   
    tree = internalBuildTree(rootDirectory, 0, '', '.') 
    return tree
    

def run():
    '''
    conducts the script
    '''
    validateInputs()
    rootDirectory = findTreeRoot()
    tree = buildTree(rootDirectory)
    print(tree)

if __name__ == '__main__':
    # just for demo
    #subprocess.run(['tree'] + sys.argv[1:])
    run() 
