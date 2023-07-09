#!/usr/bin/python3
'''a script to pack static content into a tarball
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    returns the archive path if archive has been
    correctly gernerated else return nothimg
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    archive_path = local('tar -c -z -v -f versions/web_static_{}.tgz web_static'
                     .format(timestamp))
    if archive_path.success:
        return archive_path
    else:
        return None
