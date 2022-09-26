# Imports
import urllib.request
from pytube import YouTube as yt
from mutagen.mp4 import MP4, MP4Cover
import os.path

# Read the file with all the links of the songs
txtFileOfYoutubeLinks = open('Links.txt', 'r')
for link in txtFileOfYoutubeLinks.readlines():
    video = yt(link)

    print(video.channel_id)
    # # MetaData of the song
    # print(video.description.lower())
    # Musician Loop
    composer = "None"
    if video.description.lower().find("music") != -1:
        if video.description.find("Music Composer - ") != -1:
            composer = (video.description.split("Music Composer - "))[1].split("\n")[0]
        elif video.description.find("Music - ") != -1:
            composer = (video.description.split("Music - "))[1].split("\n")[0]
    elif video.description.lower().find("composer") != -1:
        if video.description.find("Composer: ") != -1:
            composer = (video.description.split("Composer: "))[1].split("\n")[0]
    print(composer)

    # Singers Loop
    artist = "None"
    if video.description.lower().find("singer") != -1:
        if video.description.find("Singers – ") != -1:
            artist = (video.description.split("Singers – "))[1].split("\n")[0]
        elif video.description.find("Singer - ") != -1:
            artist = (video.description.split("Singer - "))[1].split("\n")[0]
        elif video.description.find("Singers: ") != -1:
            artist = (video.description.split("Singers: "))[1].split("\n")[0]
    print(artist)

    # artwork/thumbnail to the audio file
    coverArtwork = video.thumbnail_url

    # Date of the video
    year = str(video.publish_date).split("-")[0]

    # Getting parts of the Title of the video
    title = video.title.split("|")
    titleName = title[0].split(" - ")

    # Getting the Names and Data
    songName = titleName[0]
    movieName = titleName[1]
    print(songName)
    print(movieName)

    # Create a folder for the audio files to be stored
    directory = movieName
    parentDirectory = "/Users/rahuladepu/Desktop/My Files/Audio"

    if os.path.isdir(f'{parentDirectory}/{directory}'):
        print("File Exists")
        finalDirectory = parentDirectory +"/"+directory
    else:
        print("New File")
        finalDirectory = os.path.join(parentDirectory, directory)
        os.makedirs(finalDirectory)
    print(finalDirectory)

    # Look for mp4 Audio Files
    audio = video.streams.filter(mime_type="audio/mp4")
    audioList = list(enumerate(audio))

    # Loop Condition to Number all the available audio format
    x = -1
    for i in audioList:
        print(i)
        x = x + 1

    audio[x].download(finalDirectory, filename=songName+".mp4")
    print("Successful")
    print("************************************************")

    # Mutagen library
    songPath = f'{finalDirectory}/{songName}.mp4'
    songFile = MP4(songPath)

    songFile['\xa9nam'] = songName
    print(songFile['\xa9nam'])
    songFile['\xa9alb'] = movieName
    print(songFile['\xa9alb'])
    songFile['\xa9day'] = year
    print(songFile['\xa9day'])
    songFile['\xa9wrt'] = composer
    print(songFile['\xa9wrt'])
    songFile['\xa9ART'] = artist
    print(songFile['\xa9ART'])

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


# file.close()
