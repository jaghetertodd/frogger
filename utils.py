#import necessary modules
import pygame
import time

#sets up car sprite
class Sprite():
    def __init__(self, screen, direction, dir, x_pos, y_pos, spd):
        fname = direction
        self.car_img = pygame.image.load(f"assets/sprites/street/{fname}/car1.png").convert()
        self.car_img.set_colorkey((0,0,0))
        self.car_x = x_pos
        self.car_dir = dir
        self.car_spd = spd
        self.car_y = y_pos


#checks to see where it is
    def update_position(self, screen, events):
        self.car_x += self.car_spd * self.car_dir

        # Check the position of the self.fish.
        if self.car_x >= screen.get_width() - self.car_img.get_width():
            self.car_dir = -1
            self.car_img = pygame.transform.flip(self.car_img, True, False)

        if self.car_x < 0:
            self.car_dir = 1
            self.car_img = pygame.transform.flip(self.car_img, True, False)



        # Draw the self.car.

        screen.blit(self.car_img, (self.car_x, self.car_y))

#check to see if it hit the frog
    def check_for_collisions(self,background, scr, other_car_list):
        #says game over when the frog died
        def make_splash_screen(background, scr):
            custom_font = pygame.font.Font('assets/texascrust.ttf', 128)
            text = custom_font.render('Game Over', False, (255, 69, 0))
            scr.blit(background, (0, 0))
            scr.blit(text,
                     (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 100))
            # Update the display (show to player).
            pygame.display.flip()

            # Check to see if I collide with any of the fish provided in the list.
        other_car_rect_list = []
        for cars in other_car_list:
            other_car_rect_list.append(pygame.Rect(cars.car_x, cars.car_y, int(cars.car_img.get_width() / 2),
                                                   int(cars.car_img.get_height() / 2)))

        my_rect = pygame.Rect(self.frog_x, self.frog_y, int(self.frog_img.get_width() / 2),
                              int(self.frog_img.get_height() / 2))

        # Check me against all the list of fish of rectangles.
        indices_0 = my_rect.collidelistall(other_car_rect_list)
        oh_no = pygame.mixer.Sound("assets/losemusic.mp3")
        if len(indices_0) > 0:
            make_splash_screen(background, scr)
            oh_no.play()
            time.sleep(4)
            pygame.quit()


#sets up Frog, based off of the Car sprite
class Frog(Sprite):
    def __init__(self, screen, frog_x, frog_y):
        self.key_up = 'not pressed'
        self.key_down = 'not pressed'
        self.key_left = 'not pressed'
        self.key_right = 'not pressed'
        self.frog_x = frog_x
        self.frog_y = frog_y
        self.frog_img = pygame.image.load('assets/sprites/frog/up.png').convert()
        self.frog_img.set_colorkey((0,0,0))
        self.y_bnd = screen.get_height()
        self.x_bnd = screen.get_width()
        self.frog_x_spd = (screen.get_width()/(5*60))
        self.frog_y_spd = (screen.get_height()/(5*60))

    def update_position(self, screen, events):

        # Update position based on keystrokes.
        for event in events:
            # See if user presses a key.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.key_up = 'pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/move_up.png')
                    self.frog_img.set_colorkey((0,0,0))

                if event.key == pygame.K_DOWN:
                    self.key_down = 'pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/move_down.png')
                    self.frog_img.set_colorkey((0, 0, 0))

                if event.key == pygame.K_LEFT:
                    self.key_left = 'pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/move_left.png')
                    self.frog_img.set_colorkey((0, 0, 0))

                if event.key == pygame.K_RIGHT:
                    self.key_right = 'pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/move_right.png')
                    self.frog_img.set_colorkey((0, 0, 0))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.key_up = 'not pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/up.png').convert()
                    self.frog_img.set_colorkey((0, 0, 0))

                if event.key == pygame.K_DOWN:
                    self.key_down = 'not pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/down.png')
                    self.frog_img.set_colorkey((0, 0, 0))

                if event.key == pygame.K_LEFT:
                    self.key_left = 'not pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/left.png')
                    self.frog_img.set_colorkey((0, 0, 0))

                if event.key == pygame.K_RIGHT:
                    self.key_right = 'not pressed'
                    self.frog_img = pygame.image.load('assets/sprites/frog/right.png')
                    self.frog_img.set_colorkey((0, 0, 0))

        # Update frogger based on status of keys.
        if self.key_up == 'pressed':
            self.frog_y -= self.frog_y_spd

        if self.key_down == 'pressed':
            self.frog_y += self.frog_y_spd

        if self.key_left == 'pressed':
            self.frog_x -= self.frog_x_spd

        if self.key_right == 'pressed':
            self.frog_x += self.frog_x_spd

        # Check the position of the frog
        if self.frog_x >= screen.get_width() - self.frog_img.get_width():
            self.frog_x = screen.get_width() - self.frog_img.get_width()

        if self.frog_x < 0:
            self.frog_x = 0

        if self.frog_y >= self.y_bnd:
            self.frog_y = self.y_bnd

        if self.frog_y < 0:
            self.frog_y = 0



        # set up the frog
        screen.blit(self.frog_img, (self.frog_x, self.frog_y))







#sets background
def make_background(surface):
    # Load the images.
    road = pygame.image.load('assets/sprites/street/road.png').convert()
    road.set_colorkey((0,0,0))
    grass = pygame.image.load('assets/grass.png').convert()
    grass.set_colorkey((0,0,0))



    for x in range(0, surface.get_width(), grass.get_width()):
        for y in range(0, surface.get_height(), grass.get_height()):
            surface.blit(grass, (x, y))
        print(.25 * surface.get_height())

    for x in range(0, surface.get_width(), road.get_width()):
        surface.blit(road, (x, .5*surface.get_height() - road.get_height()))

    for x in range(0, surface.get_width(), road.get_width()):
        surface.blit(road, (x, .25*surface.get_height() - road.get_height()))

    for x in range(0, surface.get_width(), road.get_width()):
        surface.blit(road, (x, .75*surface.get_height() - road.get_height()))


#class for the flag
class Home():
    def __init__(self, screen, home_x, home_y):


        self.home_img = pygame.image.load('assets/sprites/home.png').convert()
        self.home_img.set_colorkey((0,0,0))
        self.home_x = home_x
        self.home_y = home_y
        self.counter = 0


    def set_up_home(self, screen):
        screen.blit(self.home_img, (self.home_x, self.home_y))

    def made_it(self, frogger, cars):
        # cars = []
        frogger_rect = pygame.Rect(frogger.frog_x, frogger.frog_y, frogger.frog_img.get_width(),
                              frogger.frog_img.get_height())

        # Check if frog has hit flag
        home_rect = pygame.Rect(self.home_x, self.home_y, self.home_img.get_width(), self.home_img.get_height())
        did_collide = home_rect.colliderect(frogger_rect)


        flag_sfx = pygame.mixer.Sound("assets/flag.mp3")
        #do these things if the frog has hit the flag
        if did_collide:
            self.counter= self.counter+1
            flag_sfx.play()
            frogger.frog_x = 400
            frogger.frog_y = 500
            for car in cars:
                print(car.car_spd)
                car.car_spd += 1.4
                print(car.car_spd)

