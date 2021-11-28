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
        
    if id == "0003825451":
        randomNum=random.randint(1, 11)
        pygame.mixer.music.load("music/disney/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == "0004086613":
        randomNum=random.randint(1, 14)
        pygame.mixer.music.load("music/faouzia/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == "0004177330":
        randomNum=random.randint(1, 11)
        pygame.mixer.music.load("music/larenDaigle/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)

    if id == "0003825420":
        randomNum=random.randint(1, 9)
        pygame.mixer.music.load("music/niallHoran/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == "0003825428":
        randomNum=random.randint(1, 6)
        pygame.mixer.music.load("music/latin/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == "0004086602":
        randomNum=random.randint(1, 14)
        pygame.mixer.music.load("music/romance/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == "0004177315":
        randomNum=random.randint(1, 9)
        pygame.mixer.music.load("music/christian/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        
    if id == "0003825442":
        randomNum=random.randint(1, 20)
        pygame.mixer.music.load("music/pop/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)

    if id == "0004086591":
        os.system("sudo shutdown now")