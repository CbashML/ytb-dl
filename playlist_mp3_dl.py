import pafy

import os.path
import glob

url_path = "PLSwCIJ7frtJx6HAya2a_39D-p8I7v07od"
home = os.path.expanduser("~")
folder_path = os.path.join(home, "Music/")

pl_url = url_path
playlist = pafy.get_playlist(pl_url)

title = playlist['title']

title = str(title).replace(" ", "_")

folder_path = os.path.join(folder_path, title)
if not os.path.isdir(folder_path):
    os.mkdir(folder_path)

os.chdir(folder_path)

length = len(playlist['items'])

for i in range(1, length):
    best_audio = playlist['items'][i]['pafy'].getbestaudio()
    name = playlist['items'][i]['pafy'].title
    print(name)

    if not os.path.isfile(name):
        print("Downloading...")
        best_audio.download()
        print("Downloaded.\n")
    else:
        print("Already exists.\n")






