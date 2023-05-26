import os
import re
import pytube

from moviepy.editor import *

# Define function to download YouTube video
def download_video(url):
    yt = pytube.YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download()
    return yt.title

# Define function to download YouTube playlist
def download_playlist(url):
    playlist = pytube.Playlist(url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    for video_url in playlist.video_urls:
        download_video(video_url)

# Define function to convert videos to MP3 format
def convert_to_mp3():
    for file in os.listdir():
        if file.endswith(".mp4"):
            video = VideoFileClip(file)
            audio = video.audio
            audio.write_audiofile(file[:-4] + ".mp3")
            audio.close()
            video.close()
            os.remove(file)

# Prompt user for URL and download videos
url = input("Enter YouTube video or playlist URL: ")
if "playlist" in url:
    download_playlist(url)
else:
    download_video(url)

# Convert downloaded videos to MP3 format
convert_to_mp3()
