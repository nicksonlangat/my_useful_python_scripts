import os, shutil
import pathlib

desktop = pathlib.Path.home() / 'Desktop'

flutter_folder = f'{desktop}/FLUTTER'

flutter_apps = [ app.path for app in  os.scandir(flutter_folder) if app.is_dir() ]

for app in flutter_apps:
    build_folder = f"{app}/build"

    try: 
        shutil.rmtree(build_folder)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
