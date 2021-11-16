#!/usr/bin/env python3

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import pygame
import random
import time

from gpiozero import LED, Buzzer
from guizero import App, Box, Text, TextBox, warn
import csv

id = 1
pygame.init()

while True:

    reader = SimpleMFRC522()
    try:
            id, text = reader.read()
            print(id)
            print(text)
    finally:
        GPIO.cleanup()

    if id == 1:
        randomNum=random.randint(1, 10)
        pygame.mixer.music.load("music/acoustic/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        while pygame.mixer.music.get_busy():
            print("playing")
            if (input()=="s"):
                pygame.mixer.music.stop()

    if id == 2:
        randomNum=random.randint(1, 11)
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
        randomNum=random.randint(1, 11)
        pygame.mixer.music.load("music/larenDaigle/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        while pygame.mixer.music.get_busy():
            print("playing")
            if (input()=="s"):
                pygame.mixer.music.stop()

    if id == 5:
        randomNum=random.randint(1, 9)
        pygame.mixer.music.load("music/niallHoran/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        while pygame.mixer.music.get_busy():
            print("playing")
            if (input()=="s"):
                pygame.mixer.music.stop()

    if id == 6:
        randomNum=random.randint(1, 6)
        pygame.mixer.music.load("music/latin/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        while pygame.mixer.music.get_busy():
            print("playing")
            if (input()=="s"):
                pygame.mixer.music.stop()

    if id == 7:
        randomNum=random.randint(1, 8)
        pygame.mixer.music.load("music/romance/" + str(randomNum) + ".mp3")
        pygame.mixer.music.play(0)
        while pygame.mixer.music.get_busy():
            print("playing")
            if (input()=="s"):
                pygame.mixer.music.stop()