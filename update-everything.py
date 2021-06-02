import subprocess
from update_technologies_from_file import generateTags
generateTags()
subprocess.call(["update.bat"])