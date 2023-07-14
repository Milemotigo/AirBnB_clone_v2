#!/usr/bin/python3
'''a script to pack static content into a tarball
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    returns the archive path if archive has been
    correctly generated, else return nothing
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    archive_filename = 'web_static_{}.tgz'.format(timestamp)
    archive_path = 'versions/{}'.format(archive_filename)
    command = 'tar -czvf {} -C web_static .'.format(archive_path)
    result = local(command)
    if result.succeeded:
        return archive_path
    else:
        return None
