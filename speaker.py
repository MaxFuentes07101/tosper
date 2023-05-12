
from gtts import gTTS
import os
import pygame

class Speaker:
    def __init__(self):
        pygame.mixer.init()

    def speak(self, text):
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save("temp.mp3")
        pygame.mixer.music.load("temp.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        os.remove("temp.mp3")
