from gtts import gTTS
import os
import pygame
mytext = 'Amo farofa!'
language = 'pt-br'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
os.system("start welcome.mp3")
# Initialize the mixer module
pygame.mixer.init()

# Load the mp3 file
pygame.mixer.music.load("welcome.mp3")

# Play the loaded mp3 file
pygame.mixer.music.play()