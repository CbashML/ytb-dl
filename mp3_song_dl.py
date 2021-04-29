import os.path
import sys
from pytube import YouTube

#url_path = sys.argv[1]
url_path = "?v=c5ZsSm45JV8"
home = os.path.expanduser("~")
folder_path = os.path.join(home, "Music/")

if len(sys.argv) > 1:
    folder_path = os.path.join(folder_path, sys.argv[2])
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
# creating YouTube object
yt = YouTube(url_path)
print("Downloading")
# accessing audio streams of YouTube obj.(first one, more available)
stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first()

# download into working directory
stream.download(folder_path)