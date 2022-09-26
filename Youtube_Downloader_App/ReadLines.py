
txtFileOfYoutubeLinks = open('Links.txt', 'r')
for line in txtFileOfYoutubeLinks.readlines():
    songName = line.split("||")[0]
    print(songName)
    Artist = line.split("||")[1]
    print(Artist)
    Album = line.split("||")[2]
    print(Album)
    Composer = line.split("||")[3]
    print(Composer)
    Year = line.split("||")[4]
    print(Year)
    linkURL = line.split("||")[5]
    print(linkURL)