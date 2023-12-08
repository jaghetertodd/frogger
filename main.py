#citing ChatGPT for suggestions on how to display a running score
from pygame import mixer
import pygame
import time

from utils import *

#start game
pygame.init()



#set up the screen
scr_wid = 800
scr_hgt = 600
scr = pygame.display.set_mode((scr_wid, scr_hgt))

#set up the individual sprites
player = Frog(scr, 400, 500) #set up player sprite
'player2 = Frog(scr, 200, 500)'
#Middle car-sprites
car = Sprite(scr, 'right', 1, 0, 250, 1.2)
car2 = Sprite(scr, 'left', -1, 750, 250, 1.2)
#Cars closest to the flag
car5 = Sprite(scr, 'left', -1, 750, 100, 1.1)
car3 = Sprite(scr, 'right', 1, 0, 100, 1.1)
#cars closest to spawn
car6 = Sprite(scr, 'left', -1, 750, 400, 1)
car4 = Sprite(scr, 'right', 1, 0, 400, 1)
#flag
house = Home(scr, 400, 30)

clock = pygame.time.Clock()

mixer.init()
mixer.music.load('assets/arcadia.ogg')
mixer.music.play()

#set up background
background = scr.copy()
make_background(background)


#sets caption of screen
pygame.display.set_caption('Revenge of the Frogger')

running = True
while running:
    font = pygame.font.Font(None, 36)

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Puts background on the scr canvas.
    scr.blit(background, (0, 0))

    #sets up sprites on the game
    player.update_position(scr,events)
    'player2.update_position(scr,events)'
    car.update_position(scr, events)
    car2.update_position(scr, events)
    car3.update_position(scr, events)
    car4.update_position(scr, events)
    car5.update_position(scr, events)
    car6.update_position(scr, events)
    house.set_up_home(scr)
    #checks to see if the frog has hit a car
    player.check_for_collisions(background, scr, [car, car2, car3, car4, car5, car6])
    #checks to see if the frog has touched the flag
    house.made_it(player, [car, car2, car3, car4, car5, car6])

    #tracks how many times the frog has reached the flag and displays it
    text = font.render(f"Points: {house.counter}", True, 'black' )
    scr.blit(text, (scr.get_width() // 8 - text.get_width() // 2, scr.get_height() - 30 - text.get_height() // 2))

    # Display scr to screen.
    pygame.display.flip()

    clock.tick(60)
