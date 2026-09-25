import os
import shutil
import ctypes

home_dir = os.path.expanduser("~")
desktop_dir = os.path.join(home_dir, "Desktop")

target_dir = os.path.join(home_dir, "Arhiv_Desktop")

os.makedirs(target_dir, exist_ok=True)
FILE_ATTRIBUTE_HIDDEN = 0x02
ctypes.windll.kernel32.SetFileAttributesW(target_dir, FILE_ATTRIBUTE_HIDDEN)

for item_name in os.listdir(desktop_dir):
    source_item = os.path.join(desktop_dir, item_name)
    destination_item = os.path.join(target_dir, item_name)
    
    if item_name.startswith('.') or item_name.lower() == 'desktop.ini':
        continue
        
    try:
        shutil.move(source_item, destination_item)
    except Exception as e:
        print('ERROR')
