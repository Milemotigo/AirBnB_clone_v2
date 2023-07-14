#!/usr/bin/python3
'''a script to pack static content into a tarball
'''

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    returns the archive path if archive has been
    correctly generated else return nothing
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    archive_path = 'versions/web_static_{}.tgz web_static'.format(timestamp)
    command = "tar -czvf {} web_static".format(timestamp)
    put = local(command)
    if result.failed:
        return None
    else:
        return put
