import random
import pygame
from pygame import *

def music():
    #background music of game
    pygame.mixer.init()
    mixer.music.load(r'C:\Users\vimal\Desktop\aq-music\aqbackground.wav')
    mixer.music.play(-1)

def main():
    music()

main()
