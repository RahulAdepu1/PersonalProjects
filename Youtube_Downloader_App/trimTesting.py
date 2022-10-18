import tinytag
from pydub import AudioSegment
from moviepy.editor import *


finalDirectory="/Users/rahuladepu/Desktop/My Files/Audio/2022/Amtee/"
songName = "Shades Of Love Mashup"

videoConvertFile = VideoFileClip(f'{finalDirectory}/{songName}.mp4')
audioConvertFile = videoConvertFile.audio
audioConvertFile.write_audiofile(f'{finalDirectory}/{songName}.mp3')
audioConvertFile.close()
videoConvertFile.close()

# importing file from location by giving its path
sound = AudioSegment.from_mp3(f'{finalDirectory}/{songName}.mp3')

# Selecting Portion we want to cut
music_duration_in_seconds = sound.duration_seconds
EndMin = int(music_duration_in_seconds/60)
print(EndMin)
EndSec = int(music_duration_in_seconds%60)
print(EndSec)

# Time to milliseconds conversion
EndTime = EndMin*60*1000+EndSec*1000

# Opening file and extracting portion of it
extract = sound[0:EndTime]

# Saving file in required location
trimmedName = "Trimmed Audio"
extract.export(f'{finalDirectory}/{songName}.mp3', format="mp3")
#
# audio = EasyID3(f'{finalDirectory}/{trimmedName}.mp3')
# print(audio['title'])
# audio['title'] = u"Example Title"
# audio['artist'] = u"Me"
# audio['album'] = u"My album"
# audio['composer'] = u"" # clear
# audio.save()
#
# print(audio['title'])
# print(audio['artist'])

# new file portion.mp3 is saved at required location