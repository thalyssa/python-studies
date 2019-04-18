#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

f = 'liltouch.mp3'

pygame.init()
pygame.mixer.music.load(f)
pygame.mixer.music.play()
pygame.event.wait()
