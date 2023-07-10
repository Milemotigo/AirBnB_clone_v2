#!/usr/bin/env python3
'''a script to pack static content into a tarball
'''

from fabric.api import *
from datetime import datetime


env.hosts = ['3.83.18.183', '54.157.147.102']
env.users = "ubuntu"


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


def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web servers,
    using the function
    """
    if os.path.exists(archive_path):
        archive = archive_path[9:]
        fileversion = "/data/web_static/releases/" + archive_file[:-4]
        archive = "/tmp/" + archive_file

        put(archive, "/tmp/")
        run("sudo mkdir -p {}".format(fileversion))

        run("sudo tar -xzf {} -C {}/".format(archive_file, fileversion))
        run("sudo rm -rf {}".format(archive))
        run("sudo mv {}/web_static/* {}".format(fileversion,
                                                fileversion))

        run("sudo rm -rf {}/web_static".format(fileversion))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(fileversion))

        print("fileversion deployed!")
        return True

    return False
