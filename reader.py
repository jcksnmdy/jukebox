import pygame
import random
import time


id = 1
pygame.init()

if id == 1:
    randomNum=random.randint(1, 8)
    pygame.mixer.music.load("music/acoustic/" + str(randomNum) + ".mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        print("playing")
        if (input()=="s"):
            pygame.mixer.music.stop()

if id == 2:
    randomNum=random.randint(1, 8)
    pygame.mixer.music.load("music/disney/" + str(randomNum) + ".mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        print("playing")
        if (input()=="s"):
            pygame.mixer.music.stop()
if id == 3:
    randomNum=random.randint(1, 8)
    pygame.mixer.music.load("music/faouzia/" + str(randomNum) + ".mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        print("playing")
        if (input()=="s"):
            pygame.mixer.music.stop()
if id == 4:
    randomNum=random.randint(1, 8)
    pygame.mixer.music.load("music/larenDaigle/" + str(randomNum) + ".mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        print("playing")
        if (input()=="s"):
            pygame.mixer.music.stop()

if id == 5:
    randomNum=random.randint(1, 8)
    pygame.mixer.music.load("music/niallHoran/" + str(randomNum) + ".mp3")
    pygame.mixer.music.play(0)
    while pygame.mixer.music.get_busy():
        print("playing")
        if (input()=="s"):
            pygame.mixer.music.stop()