#! /usr/bin/python

from __future__ import print_function
import os, sys
import shlex
import subprocess
import argparse

def main():
    """
    execute arguments provided.
    needs better checking before execution!
    """
    try:
        arg1 = sys.argv[1]
    except:
        sys.exit(1)
    
    argstr = " ".join(sys.argv[1:])
    cmd = shlex.split(argstr)
    
    try:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        out, err = proc.communicate()
        if out:
            print(out)
    except OSError as e:
        print("ERROR: command '{}' -> {}".format(argstr, e))

if __name__ == "__main__":
    main()
