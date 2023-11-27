from gtts import gTTS
import pygame

class AusioHandler:
    def __init__(self):
        self.audio_file = None
        pygame.mixer.init()
    def text_to_speech(self):
        with open("output/output.txt", 'r') as f:
            text_content = f.read()
            tts = gTTS(text=text_content, lang='en')
            tts.save('output/output.mp3')
    def play_audio(self):
        pygame.mixer.music.load("output/output.mp3")
        pygame.mixer.music.play()
    def process_audio(self):
        if True:
            self.text_to_speech()
            self.play_audio()
