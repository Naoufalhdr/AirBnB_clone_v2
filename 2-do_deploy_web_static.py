#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using the function
do_deploy.
"""
from fabric.api import env, put, run
import os.path

env.hosts = ['100.26.172.45', '54.236.12.243']


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
        run(f"tar -xzf /tmp/{archive_filename} -C {folder_name}")

        # Delete the archive from the web server
        run(f"rm /tmp/{archive_filename}")

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run("ln -s {folder_name} /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        return False
