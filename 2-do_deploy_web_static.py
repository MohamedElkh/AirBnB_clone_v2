#!/usr/bin/python3
"""filefabric to distribute archive"""
from os import path
from fabric.api import put
from fabric.api import run
from fabric.api import env
from fabric.api import *
from datetime import datetime


env.hosts = ['100.25.166.57', '54.173.193.255']
env.user = 'ubuntu'
env.key_namefile = '~/.ssh/school'


def do_deploy(archive_path):
    """func to distribute archive web """
    try:
        if not (path.exists(archive_path)):
            return False

        put(archive_path, '/tmp/')

        tim_p = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
            releases/web_static_{}/'.format(tim_p))
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
            /data/web_static/releases/web_static_{}/'.format(tim_p, tim_p))

        run('sudo rm /tmp/web_static_{}.tgz'.format(tim_p))
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
            /data/web_static/releases/web_static_{}/'.format(tim_p, tim_p))

        run('sudo rm -rf /data/web_static/releases/\
             web_static_{}/web_static'.format(time_p))

        run('sudo rm -rf /data/web_static/current')

        run('sudo ln -s /data/web_static/releases/\
             web_static_{}/ /data/web_static/current'.format(tim_p))
    except Exception:
        return False
    return True
