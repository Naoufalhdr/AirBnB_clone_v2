#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.157.186.100", "52.86.133.13"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
"""
#!/usr/bin/python3
Fabric script to distribute an archive to web servers using the function
do_deploy.
from fabric.api import env, put, run
import os.path

env.hosts = ['54.157.186.100', '52.86.133.13']


def do_deploy(archive_path):
    Distributes an archive to web servers.
    Returns True if all operations have been done correctly, otherwise False.
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
        run(f"mv {folder_name}/web_static/* {folder_name}/")

        # Remove the now empty web_static dir
        run(f"rm -rf {folder_name}/web_static")

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run(f"ln -s {folder_name}/ /data/web_static/current")

        return True

    except Exception as e:
        return False
"""
