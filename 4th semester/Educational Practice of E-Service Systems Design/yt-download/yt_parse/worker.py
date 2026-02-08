from pytube import YouTube
from moviepy.editor import *
import os
def download(url):
    yt = YouTube(url)
    t = yt.streams.filter()
    file = t[0].download("downloads")
    basePath, extension = os.path.splitext(file)
    video_f = VideoFileClip(os.path.join(basePath + ".mp4"))
    video_f.audio.write_audiofile(os.path.join(basePath + ".mp3"), verbose=False, logger=None)
    audio_f = os.path.abspath(f"{basePath}.mp3")
    return audio_f
