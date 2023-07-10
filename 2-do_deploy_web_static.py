#!/usr/bin/python3
 """ 
    Fabric script that distributes an archive to your web servers,
    using the function
 """
 from fabric.api import *
 import os.path
 env.hosts = ['34.148.10.186', '34.74.50.110']
 env.user = 'ubuntu'
  
  
 def do_deploy(archive_path):
     """
     Deploy archive to web server
     """
     if os.path.isfile(archive_path) is None:
         return False
     try:
         file = archive_path.split("/")[-1]
         rm_ext = filename.split(".")[0]
         path_rm_ext = "/data/web_static/releases/{}/".format(rm_ext)
         symlink = "/data/web_static/current"
         put(archive_path, "/tmp/")
         run("mkdir -p {}".format(path_rm_ext)) 
         run("tar -xzf /tmp/{} -C {}".format(file, path_rm_ext))
         run("rm /tmp/{}".format(file))
         run("mv {}web_static/* {}".format(path_rm_ext, path_rm_ext)) 
         run("rm -rf {}web_static".format(path_rm_ext))
         run("rm -rf {}".format(symlink)) 
         run("ln -s {} {}".format(path_rm_ext, symlink))
         return True
     except:
         return False
