#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from datetime import datetime
from fabric.api import *
import os

env.host = ["54.208.47.42", "35.175.64.254"]
env.user = "ubuntu"

def do_pack():
    """
        return the archive path if archive has generated correctly.
    """
