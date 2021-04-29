import sys
import os

import pafy
from pydub import AudioSegment


class MP3Downloader:
    """
    MP3Downloader let you download audio stream in mp3 format in your Music folder (MacOS/Unix).

    - If you going to download a playlist, it'wll be downloaded in a new folder "Playlist_Name".
    - If you want download in a sub-folder, you can use a second argument "New_Sub_Folder".

    usage:
        python3 mp3_dl.py 'PLBnJv6rImVe9g7FjZj5EyobkpVvtalRxU' 'anotherFolder'
    """

    def __init__(self, **kwargs):
        print("__init__")
        self.url = kwargs['url']
        print(self.url)
        self.folder_path = self.__get_folder_path()
        print(self.folder_path)


    def __get_folder_path(self):
        home = os.path.expanduser("~")
        folder_path = os.path.join(home, "Music/")

        if len(sys.argv) > 2:
            folder_path = os.path.join(folder_path, sys.argv[2])
            self.__create_dir(folder_path)

        if self.__is_playlist():
            folder_path = self.__join_playlist_title_to_folder_path(folder_path)

        return folder_path

    def __create_dir(self, folder_path):
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)

    def __join_playlist_title_to_folder_path(self, folder_path):
        playlist = pafy.get_playlist(self.url)
        playlist_title = playlist['title']
        playlist_title = self.__prettify_tittle(playlist_title)
        folder_path = os.path.join(folder_path, playlist_title)
        self.__create_dir(folder_path)
        return folder_path

    def __prettify_tittle(self, title):
        title.replace(" - ", "-")
        title.replace(" ", "_")
        return title

    def __is_playlist(self):
        return len(self.url) > 11

    def __song_downloader(self, name, audio_file):
        print(name)
        if not os.path.isfile(name):
            print("Downloading...")
            audio_file.download()
            print("Converting...")
            self.__convert_from_webm_to_mp3(name)
            print("Downloaded.\n")
        else:
            print("Already exists.\n")

    def __convert_from_webm_to_mp3(self, name):
        webm_filename = os.path.splitext(os.path.basename(name))[0] + '.webm'
        mp3_filename = os.path.splitext(os.path.basename(name))[0] + '.mp3'
        print(mp3_filename)
        AudioSegment.from_file(webm_filename).export(mp3_filename, format='mp3')
        os.remove(webm_filename)

    def __playlist_dowloader(self):
        playlist = pafy.get_playlist(self.url)
        length = len(playlist['items'])
        for i in range(1, length):
            best_audio = playlist['items'][i]['pafy'].getbestaudio()
            name = playlist['items'][i]['pafy'].title
            self.__song_downloader(name, best_audio)

    def download(self):
        os.chdir(self.folder_path)
        if self.__is_playlist():
            self.__playlist_dowloader()
        else:
            best_audio, name = self.__get_song_params()
            self.__song_downloader(name, best_audio)

    def __get_song_params(self):
        song = pafy.new(url=self.url)
        best_audio = song.getbestaudio()
        name = song.title
        return best_audio, name


def main(opt=""):
    print("main()")
    if not len(sys.argv) > 1:
        print("- Please introduce the url ID of the (song/list) '?list=PLBnJv6rImVe9g7FjZj5EyobkpVvtalRxU' \n"
              "- usage: python3 mp3_dl.py 'PLBnJv6rImVe9g7FjZj5EyobkpVvtalRxU' 'Optional_New_Sub-Folder' \n")
        return
    url = sys.argv[1]
    mp3_dl = MP3Downloader(url=url)
    mp3_dl.download()


if __name__ == '__main__':
    main()
