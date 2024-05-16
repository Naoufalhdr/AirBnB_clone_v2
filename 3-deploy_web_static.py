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
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive on the web server
        archive_filename = os.path.basename(archive_path)
        folder_name = f"/data/web_static/releases/{archive_filename[:-4]}"
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, folder_name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(archive_filename))

        # Move the contents of the uncompressed folder to its parent dir
        run("mv {}/web_static/* {}".format(folder_name, folder_name))

        # Remove the now empty web_static dir
        run("rm -rf {}/web_static".format(folder_name))

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run("ln -s {} /data/web_static/current".format(folder_name))

        print("New version deployed!")
        return True

    except Exception as e:
        return False


def deploy():
    """
    Deploy the web_static content to web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)