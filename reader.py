import pygame
import random
import time

from gpiozero import LED, Buzzer
from guizero import App, Box, Text, TextBox, warn
import csv

id = 1
pygame.init()
 
 
def checkRFidTag():
 	tagId = rfidText.value
	print(tagId)
	return tagId
 
print("Checking in 3")
time.sleep(1)
print("Checking in 2")
time.sleep(1)
print("Checking in 1")
time.sleep(1)

checkRFidTag()

if id == checkRFidTag():
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