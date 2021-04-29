import sys

import os
import glob
from pydub import AudioSegment

home = os.path.expanduser("~")
folder_path = os.path.join(home, "Music/Marron_5's_Greatest_Hits")
extension_list = ('*.mp4', '*.webm')

if len(sys.argv) > 1 and sys.argv[1]:
    folder_path = os.path.join(folder_path, sys.argv[1])
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)

os.chdir(folder_path)
for extension in extension_list:
    for audio in glob.glob(extension):
        webm_filename = os.path.splitext(os.path.basename(audio))[0] + '.webm'
        mp3_filename = os.path.splitext(os.path.basename(audio))[0] + '.mp3'
        print(mp3_filename)
        AudioSegment.from_file(audio).export(mp3_filename, format='mp3')
        os.remove(webm_filename)