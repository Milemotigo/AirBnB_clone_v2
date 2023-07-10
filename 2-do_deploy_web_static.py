#!/usr/bin/env python3
"""
A Python script that distributes an archive to your web servers.
"""
from fabric.api import env, put, run

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
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_rmExt))
        run("tar -xzf /tmp/{} -C {}".format(file, path_rmExt))
        run("rm /tmp/{}".format(file))
        run("mv {}web_static/* {}".format(path_rmExt, path_rmExt))
        run("rm -rf {}web_static".format(path_rmExt))
        run("rm -rf {}".format(symlink))
        run("ln -s {} {}".format(path_rmExt, symlink))
        return True
    except Exception as e:
        return False
