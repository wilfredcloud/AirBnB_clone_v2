#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generate a tgz archive"""
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        archive_path = "versions/{}".format(archive_name)
        # Create the versions directory if it doesn't exist
        local("mkdir -p versions")
        result = local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None
