#!/usr/bin/python3
"""
AirBnB clone - Deploy static using fabric
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ['3.83.18.183', '54.157.147.102']


def do_pack():
    """
    Returns the archive path if archive has been
    correctly gernerated else return None
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_pathh = "versions/web_static_{}.tgz".format(date)
    tgz_archive = local("tar -cvzf {} web_static".format(archive_pathh))

    if tgz_archive.succeeded:
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
        newFile = "/data/web_static/releases/" + archive[:-4]
        archive = "/tmp/" + archive

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newFile))

        run("sudo tar -xzvf {} -C {}/".format(archive, newFile))
        run("sudo rm -rf {}".format(archive))
        run("sudo mv {}/web_static/* {}".format(newFile,
                                                newFile))

        run("sudo rm -rf {}/web_static".format(newFile))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newfileversion))
        print("Success")
        return True
    else:
        return False

def deploy():
    """
    creates and distributes an archive to your web servers
    """
    archive_path = do_pack
    if not path:
        return False
    else:
        do_deploy(archive_path)
