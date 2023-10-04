#!/usr/bin/python3
"""filefabric to distribute archive script based on file web static"""
import os
from fabric.api import env, local, put, run, runs_once
from datetime import datetime


env.hosts = ['100.25.166.57', '54.173.193.255']
env.user = 'ubuntu'
env.key_namefile = '~/.ssh/school'


def do_deploy(archive_path):
    """func to distribute archive web"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
