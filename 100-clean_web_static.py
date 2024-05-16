#!/usr/bin/python3
"""
Fabric script to delete out-of-date archives using the function do_clean.
"""
from fabric.api import env, run, local
import os

env.hosts = ["54.157.186.100", "52.86.133.13"]


def do_clean(number=0):
    """
    Delete out-of-date archives.
    """
    try:
        # Ensure number is an integer
        number = int(number)

        # Get list of archives sorted by modification time (oldest first)
        archives = sorted(
                os.listdir("versions"),
                key=lambda x: os.path.getmtime(f"versions/{x}")
                )

        # Determine number of archives to keep
        num_to_keep = max(number, 1)

        # Delete unnecessary archives in versions folder
        for archive in archives[:-num_to_keep]:
            local(f"rm -f versions/{archive}")

        # Delete unnecessary archives on the web servers
        for archive in archives[:-num_to_keep]:
            run(f"rm -f /data/web_static/releases/{archive[:-4]}.tgz")

        return True

    except Exception as e:
        return False
