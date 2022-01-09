from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time
import configparser
import re


def match_rule(filename):
    for index, rule in enumerate(rules):
        if re.search(config["RULES"][rule], filename) is not None:
            return index


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(source_folder):
            src = f"{source_folder}/{filename}"
            if os.path.isdir(src):
                continue
            rule_index = match_rule(filename)
            dest = f"{source_folder}/"
            output_folder = None
            if rule_index is None:
                dest += f"{config['MAIN']['default']}/{filename}"
            else:
                output_folder = config['FOLDERS'][f'folder{rule_index}']
                dest += f"{output_folder}/{filename}"
            try:
                os.rename(src, dest)
            except FileNotFoundError:
                print(f"Output folder '{output_folder}' not found")


try:
    config = configparser.ConfigParser()
    config.read(f"{os.path.dirname(os.path.abspath(__file__))}/config.ini")
    source_folder = config["MAIN"]["source"]
    rules = [rule for rule in config["RULES"]]
    folders = [folder for folder in config["FOLDERS"]]
except KeyError:
    print("Incorrect or missing config file")
    exit(-1)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, source_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except:
    observer.stop()
observer.join()
