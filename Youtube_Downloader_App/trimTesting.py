from pydub import AudioSegment
from moviepy.editor import *

audioConveretFile = AudioFileClip("/Users/rahuladepu/Desktop/My Files/Audio/2022/Amtee/Shades Of Love Mashup.mp4")
audioConveretFile.write_audiofile("/Users/rahuladepu/Desktop/My Files/Audio/2022/Amtee/Shades Of Love Mashup.mp3")
audioConveretFile.close()

#importing file from location by giving its path
sound = AudioSegment.from_mp3("/Users/rahuladepu/Desktop/My Files/Audio/2022/Amtee/Shades Of Love Mashup.mp3")

#Selecting Portion we want to cut
StrtMin = 0
StrtSec = 0
EndMin = 0
EndSec = 21

# Time to milliseconds conversion
StrtTime = StrtMin*60*1000+StrtSec*1000
EndTime = StrtMin*60*1000+EndSec*1000

# Opening file and extracting portion of it
extract = sound[StrtTime:EndTime]

# Saving file in required location
extract.export("/Users/rahuladepu/Desktop/My Files/Audio/2022/Amtee/trimmed.mp3", format="mp3")

# new file portion.mp3 is saved at required location