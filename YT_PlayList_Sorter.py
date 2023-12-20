import os
import yt_dlp

# Specify the folder where the downloaded files are located
path = "YOUR PATH"

# Get the list of files in the folder
files = os.listdir(path)

# Get the list of videos available in the YouTube playlist
playlist_url = "A YOUTUBE PLAYLIST"
ydl = yt_dlp.YoutubeDL()
playlist = ydl.extract_info(playlist_url, download=False)

# Comparison of file names with playlist video names
for video in playlist["entries"]:
    for i, file in enumerate(files):
        name, ext = os.path.splitext(file)
        if name == video["title"]:
            new_name = f"{video['playlist_index']} {video['title']}{ext}"
            os.rename(os.path.join(path, file), os.path.join(path, new_name))
            files[i] = new_name

# Print the list of sorted files
for file in files:
    print(file)