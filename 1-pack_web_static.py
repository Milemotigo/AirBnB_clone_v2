#!/usr/bin/python3
'''a script to pack static content into a tarball
'''

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Returns the archive path if archive has been
    correctly gernerated else return nothimg
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    Obj_tar = local('tar -c -z -v -f versions/web_static_{}.tgz web_static'
                    .format(timestamp))
    if Obj_tar.failed:
        return None
    else:
        return Obj_tar
