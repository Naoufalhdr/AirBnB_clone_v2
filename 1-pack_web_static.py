#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static
folder of the AirBnB Clone repo.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Create the file name based on current date and time
        now = datetime.now()
        file_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

        # Compress the contents of the web_static folder into the .tgz file
        local("tar -cvzf versions/{} ./web_static".format(file_name))

        # Return the archive path if generated successfully
        return "versions/{}".format(file_name)
    except Exception as e:
        return None
