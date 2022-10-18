# Imports
import urllib.request
from pytube import YouTube as yt
from mutagen.mp4 import MP4, MP4Cover
import os.path
from moviepy.editor import *

songCount = 0
downloadCount = 0
# Read the file with all the links of the songs
txtFileOfYoutubeLinks = open('Txt Files of Links/Gym Songs.txt', 'r')

# txtFileOfYoutubeLinks = open('Links.txt', 'r')
for line in txtFileOfYoutubeLinks.readlines()[2:]:

    songCount = songCount+1
    print(f'Song on line number {songCount + 2}')
    print("*****************************")

    songName = line.split("||")[0]
    print("Song Name : "+songName)
    artist = line.split("||")[1]
    print("Artist : "+artist)
    album = line.split("||")[2]
    print("Album : "+album)
    composer = line.split("||")[3]
    print("Composer : "+composer)
    year = line.split("||")[4]
    print("Year : "+year)
    linkURL = line.split("||")[5]
    # print("Link Url : "+linkURL)

    video = yt(linkURL)

    # artwork/thumbnail to the audio file
    coverArtwork = video.thumbnail_url

    # Look for mp4 Audio Files
    audio = video.streams.filter(mime_type="audio/mp4")
    audioList = list(enumerate(audio))

    # Loop Condition to Number all the available audio format
    x = -1
    for i in audioList:
        x = x + 1

    videoDirectory = "/Users/rahuladepu/Desktop/My Files/Video/Gym_Songs"

    if os.path.isfile(f'{videoDirectory}/{songName}.mp4'):
        print("File Exists")
        print("Skipping")
        print("*****************************")
    else:
        print("**** Creating a New File ****")
        audio[x].download(videoDirectory, filename=songName + ".mp4")

        downloadCount = downloadCount + 1

        # Mutagen library
        songPath = f'{videoDirectory}/{songName}.mp4'
        songFile = MP4(songPath)

        fd = urllib.request.urlopen(coverArtwork)
        # Drop the entire PIL part
        covr = MP4Cover(fd.read(), getattr(
            MP4Cover, 'FORMAT_PNG'
            if coverArtwork.endswith('png')
            else 'FORMAT_JPEG'
        ))
        fd.close()
        songFile['covr'] = [covr]  # make sure it's a list

        songFile.save()
        print(f'Successful downloaded {downloadCount} songs')
        print("*****************************")

    # # Create a folder for the audio files to be stored
    # directory = "Gym_Songs"
    # parentDirectory = "/Users/rahuladepu/Desktop/My Files/Audio/"
    #
    # if os.path.isdir(f'{parentDirectory}/{directory}'):
    #     print("Folder Exists")
    #     finalDirectory = parentDirectory + "/" + directory
    # else:
    #     print("**** Creating a New Folder ****")
    #     finalDirectory = os.path.join(parentDirectory, directory)
    #     os.makedirs(finalDirectory)
    #
    # if os.path.isfile(f'{videoDirectory}/{songName}.mp4'):
    #     print("File Exists")
    #     print("Skipping")
    #     print("*****************************")
    # else:
    #     print("**** Creating a New File ****")
    #     videoConvertFile = VideoFileClip(f'{finalDirectory}/{songName}.mp4')
    #     audioConvertFile = videoConvertFile.audio
    #     audioConvertFile.write_audiofile(f'{finalDirectory}/{songName}.mp3')
    #     audioConvertFile.close()
    #     videoConvertFile.close()
print("********** All Done *********")
print("*****************************")