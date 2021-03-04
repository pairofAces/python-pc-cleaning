from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != "Personal":
                new_name = filename
                file_exists = os.path.isfile(folder_destination + '/' + new_name)
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str[i] + os.path.splitext(folder_to_track + '/' + new_name)[1]
                    new_name = new_name.split('/')[4]
                    file_exists = os.path.isfile(folder_destination + '/' + new_name)
                
                src = folder_to_track + '/' + filename
                new_name = folder_destination + '/' + new_name
                os.rename(src, new_name)

# create a dictionary with file types pointing to destinations
extensions_folders = {
    '.aif' : '/Users/karanchauhan/Music/Downloaded',
    '.cda' : '/Users/karanchauhan/Music/Downloaded',
    '.mid' : '/Users/karanchauhan/Music/Downloaded',
    '.midi' : '/Users/karanchauhan/Music/Downloaded',
    '.mp3' : '/Users/karanchauhan/Music/Downloaded',
    '.mpa' : '/Users/karanchauhan/Music/Downloaded',
    '.ogg' : '/Users/karanchauhan/Music/Downloaded',
    '.wav' : '/Users/karanchauhan/Music/Downloaded',
    '.wma' : '/Users/karanchauhan/Music/Downloaded',
    '.wpl' : '/Users/karanchauhan/Music/Downloaded',

    '.txt' : '/Users/karanchauhan/Documents/TextFiles',
}

# folder_to_track = '/Users/karanchauhan/Downloads'
folder_to_track = '/Users/karanchauhan/Desktop'
folder_destination = '/Users/karanchauhan/Desktop/Personal'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()