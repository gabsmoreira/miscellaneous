from gtts import gTTS
import os
tts = gTTS(text='Good night Gabriel', lang='en')
tts.save("good.mp3")
print(os.getcwd())
os.system("good.mp3")
