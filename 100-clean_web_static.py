#!/usr/bin/python3
# fabric file to delete out dated archive
import os
from fabric.api import *

env.hosts = ['100.25.166.57', '54.173.193.255']


def do_clean(number=0):
    """func to delete out dated archvies"""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))

    [archives.pop() for x in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(d)) for d in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()

        archives = [d for d in archives if "web_static_" in d]

        [archives.pop() for x in range(number)]
        [run("rm -rf ./{}".format(d)) for d in archives]
