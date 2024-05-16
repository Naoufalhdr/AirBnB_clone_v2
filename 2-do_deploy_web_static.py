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

    try:
        # Upload the archive to the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive on the web server
        archive_filename = os.path.basename(archive_path)
        folder_name = f"/data/web_static/releases/{archive_filename[:-4]}"
        run(f"mkdir -p {folder_name}")
        run(f"tar -xzf /tmp/{archive_filename} -C {folder_name}/")

        # Delete the archive from the web server
        run(f"rm /tmp/{archive_filename}")

        # Move the contents of the uncompressed folder to its parent dir
        run(f"mv {folder_name}/web_static/* {folder_name}")

        # Remove the now empty web_static dir
        run(f"rm -rf {folder_name}/web_static")

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run(f"ln -s {folder_name}/ /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        return False
