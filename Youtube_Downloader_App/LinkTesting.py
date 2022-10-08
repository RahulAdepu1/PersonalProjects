from pytube import YouTube as yt

link = "https://youtu.be/H3a-eT7Vge0"
video = yt(link)

print(video.title)