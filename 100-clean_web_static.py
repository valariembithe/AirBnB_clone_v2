#!/usr/bin/python3
"""Function that deploys """
from fabric.api import *

env.hosts = ['54.208.47.42', '35.175.64.254']
env.user = "ubuntu"

def do_clean(number=0):
    """Cleans """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1
