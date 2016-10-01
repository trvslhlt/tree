#!/usr/bin/env python3
import functools
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
        return
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
    directoryCount = [0]
    fileCount = [0]

    def internalBuildTree(directory, level, lineHead, tree):
        names = os.listdir(directory)
        names = alphnumSort(names)
        names = list(filter(lambda x: x[0] is not '.', names))
        for idx, name in enumerate(names):
            if name.startswith('.'):
                continue
            namepath = os.path.join(directory, name)
            hatPipe = '├'
            if idx == len(names) - 1:
                hatPipe = '└'
            tree = tree + '\n'+ lineHead +  hatPipe + '── ' + name
            if os.path.isdir(namepath):
                directoryCount[0] += 1
                descender = "    " if idx == (len(names) - 1) else "│   "
                tree = internalBuildTree(namepath, level + 1, lineHead + descender, tree)
            else:
                fileCount[0] += 1
        return tree
    firstLine = '.'
    if len(sys.argv) is 2:
        firstLine = sys.argv[1]
    tree = internalBuildTree(rootDirectory, 0, '', firstLine)
    report = str(directoryCount[0]) + ' directories, ' + str(fileCount[0]) + ' files'
    return tree, report


def alphnumSort(l):

    def alphCmp(e1, e2):

        def trimNonalpnumFromHead(e):
            e_cp = e
            while len(e)is not 0 and not e_cp[0].isalnum():
                e_cp = e_cp[1:]
            return e_cp
        e1_cp = trimNonalpnumFromHead(e1)
        e2_cp = trimNonalpnumFromHead(e2)
        return -1 if e1_cp.lower() < e2_cp.lower() else 1
    return sorted(l, key=functools.cmp_to_key(alphCmp))


def run():
    '''
    conducts the script
    '''
    validateInputs()
    rootDirectory = findTreeRoot()
    tree, report = buildTree(rootDirectory)
    sys.stdout.buffer.write(tree.encode('utf-8'))
    print('\n')
    print(report)


if __name__ == '__main__':
    run()
