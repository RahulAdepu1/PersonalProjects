# Imports
import urllib.request
from pytube import YouTube as yt
from mutagen.mp4 import MP4, MP4Cover

txtFileOfYoutubeLinks = open('Txt Files of Links/Gym Songs.txt', 'r')

songCount = 0
# Read the file with all the links of the songs

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

    # Create a folder for the audio files to be stored
    directory = year+"/"+album
    parentDirectory = "/Users/rahuladepu/Desktop/My Files/Audio/Gym_Songs"

    # Mutagen library
    songPath = f'{parentDirectory}/{songName}.m4a'
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
    print(f'Added metadata to {songCount} songs')
    print("*****************************")
print("********** All Done *********")
print("*****************************")