# TOCAR MÚSICA DIRETO DO PYTHON 

import pygame #possui diversas funcionalidaded de games
pygame.init() #inicia o pygame 
pygame.mixer.music.load('faixa06.mp3')
pygame.mixer.music.play()
pygame.event.wait()