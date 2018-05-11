#! /usr/bin/python

import os, sys
import shlex, subprocess
import argparse

try:
    arg1 = sys.argv[1]
except:
    sys.exit(1)

cmd = shlex.split(" ".join(sys.argv[1:]))

proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out, err = proc.communicate()
if out:
    print(out)

