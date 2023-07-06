from fabric.api import local
from datetime import datetime


def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder."""
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month,
            now.day, now.hour,
            now.minute, now.second)
    archive_path = "versions/{}".format(archive_name)

    local("mkdir -p versions")
    result = local("tar -czvf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None
