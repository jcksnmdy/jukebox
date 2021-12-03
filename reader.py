#!/usr/bin/env python3
import pygame
import random
import time
import os
from datetime import datetime
import threading

def keepAwake():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time[3:5])
        if (int(current_time[3:5])/5==0) and not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("music/silence.mp3")
            print("playing silence")
            pygame.mixer.music.play(0)
        time.sleep(30)

awake = threading.Thread(group=None, target=keepAwake, name=None)
awake.start()
run = True
def playSongs(playlist, songs):
    while run:
            randomNum=random.randint(1, songs)
            pygame.mixer.music.load("music/" + playlist + "/" + str(randomNum) + ".mp3")
            pygame.mixer.music.play(0)
            while pygame.mixer.music.get_busy():
                time.sleep(1)

pygame.init()

playerSongs = threading.Thread(group=None, target=playSongs, args=("faouzia", 14, ), name=None)
#playerSongs.start()
#playerSongs.join()

id = 1

vol = 40
os.system("ifconfig")
os.system("amixer set Master " + str(vol) + "%")

while True:
    playerSongs
    id = input("Card")

    if id == "0004086624":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("acoustic", 10, ), name=None)
        playerSongs.start()
        
    if id == "0003825451":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("disney", 11, ), name=None)
        playerSongs.start()
        
    if id == "0004086613":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("faouzia", 14, ), name=None)
        playerSongs.start()
        
    if id == "0004177330":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("larenDaigle", 12, ), name=None)
        playerSongs.start()

    if id == "0003825420":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("niallHoran", 9, ), name=None)
        playerSongs.start()
        
    if id == "0003825428":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("latin", 6, ), name=None)
        playerSongs.start()
        
    if id == "0004086602":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("romance", 14, ), name=None)
        playerSongs.start()
        
    if id == "0004177315":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("christian", 9, ), name=None)
        playerSongs.start()
        
    if id == "0003825442":
        pygame.mixer.music.stop()
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        run = True
        playerSongs = threading.Thread(group=None, target=playSongs, args=("pop", 20, ), name=None)
        playerSongs.start()

    if id == "0003487172":
        os.system("sudo shutdown now")

    if id == "0004086591":
        pygame.mixer.music.stop()

        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")

        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")
        
        if (playerSongs.is_alive()):
            run = False
            playerSongs.join()
            print("Stopped")

    if id == "0003466871":
        if (vol < 100):
            vol += 10
        os.system("amixer set Master " + str(vol) + "%")

    if id == "0003466854":
        if (vol > 0):
            vol -= 10
        os.system("amixer set Master " + str(vol) + "%")