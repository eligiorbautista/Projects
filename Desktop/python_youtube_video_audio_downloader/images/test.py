import os, shutil

from pytube import YouTube

# Where to save
save_path = '~/Downloads'

youtube_video = YouTube('asdasd') # Put the url here

# Note : Progressive streams have the video and audio in a single file, 
# but typically do not provide the highest quality media
# Filter out all the files with "mp4" extension or audio

youtube_video.streams.filter(only_audio=True)

# Get the video with the extension and resolution
# passed in the get() function
youtube_video = youtube_video.streams.get_highest_resolution()
output_file = youtube_video.download(r'~/Downloads') # Put the save path here and download the video


filename, exe = os.path.splitext(output_file)
new_file = filename + '.mp3'
os.rename(output_file, new_file)

