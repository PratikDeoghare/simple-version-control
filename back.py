#! /usr/bin/env python

import fnmatch, shutil, stat
import os, sys

def next_version(filename):
    return len([1 for f in os.listdir('.') if fnmatch.fnmatch(f, filename + '*')])

# tagging 

if __name__ == '__main__':
    filename = sys.argv[1]
    msg = ''
    if len(sys.argv) > 2:
        msg = sys.argv[2]
    filename1 = '.'.join([filename, str(next_version(filename)), msg])
    shutil.copyfile(filename, filename1)
    os.chmod(filename1, 0444)





