# This script is currently designed for Windows only.
# Changes to detect OS and correct Kodi path are always welcome
# WARNING: YOU MUST INSTALL THE ADDON USING THE BUILD SCRIPT FIRST
import os
import shutil
import sys

src_dir = os.path.dirname(os.path.realpath(__file__))
dst_dir = os.path.join(os.getenv('APPDATA'), 'Kodi', 'addons', 'plugin.video.addonstatetest')

# Check if destination directory exists
if not os.path.exists(dst_dir):
    print("Error: The directory 'plugin.video.addonstatetest' does not exist. Please install the addon using the build script first.")
    sys.exit(1)

items_to_copy = ['lib', 'resources', 'addon.py', 'addon.xml', 'LICENSE']

for item in items_to_copy:
    src_item = os.path.join(src_dir, item)
    dst_item = os.path.join(dst_dir, item)
    if os.path.isdir(src_item):
        if os.path.exists(dst_item):
            shutil.rmtree(dst_item)
        shutil.copytree(src_item, dst_item)
    else:
        shutil.copy2(src_item, dst_item)
