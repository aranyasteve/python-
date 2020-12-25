from gtts import gTTS
import os


a = "Hello i am your assistant"
l = 'en'
output = gTTS(text=a, lang=l, slow=False)