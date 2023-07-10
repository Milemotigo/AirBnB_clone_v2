#!/usr/bin/env python3
'''a script to pack static content into a tarball
'''

from fabric.api import *
from datetime import datetime


def do_pack():
    """
    returns the archive path if archive has been
    correctly gernerated else return nothimg
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    local('mkdir -p versions')
    archive_path = local('tar -c -z -v -f versions/web_static_{}.tgz\
            web_static'.format(timestamp))
    if archive_path.success:
        return archive_path
    else:
        return None


env.hosts = ['3.83.18.183', '54.157.147.102']


def do_deploy(archive_path):
    """
    Deploy the archive to web servers.
    """
    if not os.path.isfile(archive_path):
        return False
    try:
        file = archive_path.split('/')[-1]
        rmExt = file.split('.')[0]
        path_rmExt = '/data/web_static/release/{}/'.format(rmExt)
        symlink = '/data/web_static/current'
        put(sudo archive_path, "/tmp/")
        run(sudo "mkdir -p {}".format(path_rmExt))
        run(sudo "tar -xzf /tmp/{} -C {}".format(file, path_rmExt))
        run(sudo "rm /tmp/{}".format(file))
        run(sudo "mv {}web_static/* {}".format(path_rmExt, path_rmExt))
        run(sudo "rm -rf {}web_static".format(path_rmExt))
        run(sudo "rm -rf {}".format(symlink))
        run(sudo "ln -s {} {}".format(path_rmExt, symlink))
        return True
    except Exception as e:
        return False
