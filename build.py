import os
import shutil
import zipfile

src_dir = os.path.dirname(os.path.realpath(__file__))
dst_dir = os.path.join(src_dir, 'dist', 'plugin.video.addonstatetest')

os.makedirs(dst_dir, exist_ok=True)

items_to_copy = ['lib', 'resources', 'addon.py', 'addon.xml', 'LICENSE']

for item in items_to_copy:
    src_item = os.path.join(src_dir, item)
    dst_item = os.path.join(dst_dir, item)
    if os.path.isdir(src_item):
        shutil.copytree(src_item, dst_item)
    else:
        shutil.copy2(src_item, dst_item)

with zipfile.ZipFile(os.path.join(src_dir, 'dist', 'plugin.video.addonstatetest.zip'), 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(dst_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), dst_dir))

shutil.rmtree(dst_dir)