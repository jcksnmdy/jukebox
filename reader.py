#!/usr/bin/env python3
import pygame
import random
import time
import os

id = 1
pygame.init()

while True:

    id = input("Card")

    if id == "0004086624":
        randomNum=random.randint(1, 10)
        pygame.mixer.music.load("music/acoustic/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == 2:
        randomNum=random.randint(1, 11)
        pygame.mixer.music.load("music/disney/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == 3:
        randomNum=random.randint(1, 14)
        pygame.mixer.music.load("music/faouzia/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == 4:
        randomNum=random.randint(1, 11)
        pygame.mixer.music.load("music/larenDaigle/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)

    if id == 5:
        randomNum=random.randint(1, 9)
        pygame.mixer.music.load("music/niallHoran/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == 6:
        randomNum=random.randint(1, 6)
        pygame.mixer.music.load("music/latin/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == 7:
        randomNum=random.randint(1, 14)
        pygame.mixer.music.load("music/romance/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == 8:
        randomNum=random.randint(1, 9)
        pygame.mixer.music.load("music/christian/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == 9:
        randomNum=random.randint(1, 20)
        pygame.mixer.music.load("music/pop/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)

    if id == 10:
        os.system("sudo shutdown now")