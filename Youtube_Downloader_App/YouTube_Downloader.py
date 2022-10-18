# Imports
import urllib.request
from pytube import YouTube as yt
from mutagen.mp4 import MP4, MP4Cover
import os.path
from moviepy.editor import *

count = 0
# Read the file with all the links of the songs
txtFileOfYoutubeLinks = open('Test_File.txt', 'r')

# txtFileOfYoutubeLinks = open('Links.txt', 'r')
for line in txtFileOfYoutubeLinks.readlines():
    count = count+1
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
    print("Link Url : "+linkURL)

    video = yt(linkURL)

    # artwork/thumbnail to the audio file
    coverArtwork = video.thumbnail_url

    # Look for mp4 Audio Files
    audio = video.streams.filter(progressive=True)
    audioList = list(enumerate(audio))

    # Loop Condition to Number all the available audio format
    x = -1
    for i in audioList:
        # print(i)
        x = x + 1

    # Create a folder for the audio files to be stored
    directory = year+"/"+album
    parentDirectory = "/Users/rahuladepu/Desktop/My Files/Audio/"

    if os.path.isdir(f'{parentDirectory}/{directory}'):
        print("Folder Exists")
        finalDirectory = parentDirectory + "/" + directory
    else:
        print("**** Creating a New Folder ****")
        finalDirectory = os.path.join(parentDirectory, directory)
        os.makedirs(finalDirectory)

    if os.path.isfile(f'{finalDirectory}/{songName}.mp4'):
        print("File Exists")
        print("Skipping")
        print("*****************************")
    else:
        print("**** Creating a New File ****")
        audio[x].download(finalDirectory, filename=songName + ".mp4")

        # Mutagen library
        songPath = f'{finalDirectory}/{songName}.mp4'
        songFile = MP4(songPath)

        songFile['\xa9nam'] = songName
        # print(songFile['\xa9nam'])
        songFile['\xa9alb'] = album
        # print(songFile['\xa9alb'])
        songFile['\xa9day'] = year
        # print(songFile['\xa9day'])
        songFile['\xa9wrt'] = composer
        # print(songFile['\xa9wrt'])
        songFile['\xa9ART'] = artist
        # print(songFile['\xa9ART'])

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
        print(f'Successful downloaded {count} songs')
        print("*****************************")
print("********** All Done *********")
print("*****************************")