import sys
from pytube import YouTube

path = sys.argv[1]

# creating YouTube object
yt = YouTube(path)

# accessing audio streams of YouTube obj.(first one, more available)
stream = yt.streams.filter(only_audio=True).first()
# downloading a video would be: stream = yt.streams.first()

# download into working directory
stream.download()