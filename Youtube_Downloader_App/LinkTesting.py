from pytube import YouTube as yt
# import ffmpeg

link = "https://youtu.be/H3a-eT7Vge0"
video = yt(link)

print(video.title)

audio = video.streams.filter(mime_type="audio/mp4")
audioList = list(enumerate(audio))

# Loop Condition to Number all the available audio format
x = -1
for i in audioList:
    x = x + 1

parentDirectory = "/Users/rahuladepu/Desktop/My Files/Audio/"

audio[x].download(parentDirectory, filename=video.title + ".mp3")