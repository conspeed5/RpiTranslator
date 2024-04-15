import speech_recognition as sr
import pygame
import pyaudio
import sys
from googletrans import Translator, constants
from pprint import pprint

pygame.init()

White = (255,255,255)
Black = (0,0,0)

display_surface = pygame.display.set_mode((480,350))

font = pygame.font.Font('Arial.ttf', 10)
text = ""

def TranslateText(input):
        translator = Translator(service_urls=[
        'translate.google.ie',
        'translate.google.com',
        'translate.google.co.uk',])
        output = translator.translate(input, dest='de')
        return output.text

while True:
        r = sr.Recognizer()
        speech = sr.Microphone(device_index=1)
        with speech as source:
                audio = r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
        try:
                recog = r.recognize_google(audio)
                print("You said: " + recog)
                translated = TranslateText(recog)
                text = font.render(translated, True, Black)
                textRect = text.get_rect()
                textRect.center = (480 // 2, 350 // 2)
                display_surface.fill(White)
                display_surface.blit(text,textRect)
                pygame.display.update()
        except sr.UnknownValueError:
                print("Error Recognising")
        except sr.RequestError as e:
                print("Server Communication Failed")