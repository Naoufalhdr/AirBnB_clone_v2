#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers using
the function deploy.
"""
from fabric.api import env, run, local
from fabric.operations import put
from datetime import datetime
import os

env.hosts = ['54.157.186.100', '52.86.133.13']


def do_pack():
    """
    Create a compressed archive of web_static folder.
    Returns the path to the created archive, or None if the archive creation
    fails.
    """
    try:
        # Create directory if it doesn't exist
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        # Create archive filename using current date and time
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(now)

        # Create the compressed archive
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    Returns True if all operations have been done correctly, otherwise False.
    """

    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Upload the archive to the web server
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False

    # Uncompress the archive on the web server
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False

    # Delete the archive from the web server
    if run("rm /tmp/{}".format(file)).failed is True:
        return False

    # Move the contents of the uncompressed folder to its parent dir
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False

    # Remove the now empty web_static dir
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False

    # Delete the symbolic link /data/web_static/current
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    # Create a new symbolic link /data/web_static/current
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """
    Deploy the web_static content to web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
