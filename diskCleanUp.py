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
                