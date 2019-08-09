#! /usr/bin/env python

"""
plan.py patched: this is a modified version of the file provided by the original authors
It contains some methods to resolve global paths + it saves temporary some files under temp folders
"""

import subprocess
import sys
import shutil

# to resolve the path to translate.py, preprocess and search
import rospkg
import os

def main():
    def run(*args, **kwargs):
        input = kwargs.pop('input', None)
        output = kwargs.pop('output', None)
        assert not kwargs
        redirections = {}
        if input:
            redirections['stdin'] = open(input)
        if output:
            redirections['stdout'] = open(output, 'w')
        print args, redirections
        subprocess.check_call(sum([arg.split('+') for arg in args],[]), **redirections)

    config, domain, problem, result_name = sys.argv[1:]

    # get an instance of RosPack with the default search paths
    rospack = rospkg.RosPack()

    # get the path to tfd_planner ros pkg
    base_path = rospack.get_path('tfd_planner') + '/build/tfd-src-0.4/downward/'

    # run translator
    run(base_path + 'translate/translate.py', domain, problem)

    # run preprocessing
    sas_path = os.environ['HOME'] + '/.ros/output.sas'
    run(base_path + 'preprocess/preprocess', input=sas_path)

    # run search
    search_path = os.environ['HOME'] + '/.ros/output'
    run(base_path + 'search/search', config, 'p', result_name, input=search_path)

if __name__ == '__main__':
    main()
