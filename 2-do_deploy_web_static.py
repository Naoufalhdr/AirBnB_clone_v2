#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using the function
do_deploy.
"""
from fabric.api import env, put, run
import os.path

env.hosts = ['54.157.186.100', '52.86.133.13']


def do_deploy(archive_path):
    """
    Distributes an archive to web servers.
    Returns True if all operations have been done correctly, otherwise False.
    """
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the web server
    if put(archive_path, '/tmp/').failed is True:
        return false

    # Uncompress the archive on the web server
    archive_filename = os.path.basename(archive_path)
    folder_name = f"/data/web_static/releases/{archive_filename[:-4]}"
    if run(f"mkdir -p {folder_name}").failed is True:
        return False
    if run(f"tar -xzf /tmp/{archive_filename} "
            "-C {folder_name}/").failed is True:
        return Fasle

    # Delete the archive from the web server
    if run(f"rm /tmp/{archive_filename}").failed is True:
        return False

    # Move the contents of the uncompressed folder to its parent dir
    if run(f"mv {folder_name}/web_static/* {folder_name}/").failed is True:
        return False

    # Remove the now empty web_static dir
    if run(f"rm -rf {folder_name}/web_static").failed is True:
        return False

    # Delete the symbolic link /data/web_static/current
    if run("rm -rf /data/web_static/current").failed is True:
        return False

    # Create a new symbolic link /data/web_static/current
    if run(f"ln -s {folder_name}/ /data/web_static/current").failed is True:
        return False

    print("New version deployed!")
    return True
