#!/usr/bin/python3
"""Create and distributes an archive to web servers"""
import os.path
from fabric.api import local
import time
from fabric.operations import env, put, run

env.hosts = ['54.208.47.42', '35.175.64.254']

def do_pack():
    """Generate an tgz archive from web_static folder"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
