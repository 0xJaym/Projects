# Using gTTs (Google Text to Speech)
# Online Mode
from gtts import gTTS
import os
mytext="This is my order"
l="en"
obj=gTTS(text=mytext,lang=l)
obj.save("Welcome.mp3")
os.system("vlc Welcome.mp3")

