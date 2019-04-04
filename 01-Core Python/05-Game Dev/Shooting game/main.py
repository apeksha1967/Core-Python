import pygame
import random
from pygame import font
import time
from pygame.locals import *

pygame.init()

blue = 0,0,255
red = 255,0,0
white = 255,255,255
black = 0,0,0

width = 1289
height = 718

screen = pygame.display.set_mode((width, height))

playimage = pygame.image.load("assets/images/startscreen.png")
img_1 = pygame.image.load("assets/images/background_2.png")
pointer = pygame.image.load("assets/images/aim.png")

animal_1 = pygame.image.load("assets/images/animal_1.png")
animal_2 = pygame.image.load("assets/images/animal_2.png")
animal_3 = pygame.image.load("assets/images/animal_3.png")
animal_4 = pygame.image.load("assets/images/animal_4.png")
animal_5 = pygame.image.load("assets/images/animal_5.png")
animal_6 = pygame.image.load("assets/images/animal_6.png")
animal_7 = pygame.image.load("assets/images/animal_7.png")
animal_8 = pygame.image.load("assets/images/animal_8.png")
animal_9 = pygame.image.load("assets/images/animal_9.png")
animal_10 = pygame.image.load("assets/images/animal_10.png")

animalList = [animal_1,animal_2,animal_3,animal_4,animal_5,animal_6,animal_7,animal_8,animal_9,animal_10]

sound_1 = pygame.mixer.Sound("assets/music/gunshot_2.wav")
sound_2 = pygame.mixer.Sound("assets/music/gameover_2.wav")

clock = pygame.time.Clock()
FPS = 100

gunImage = pygame.image.load('assets/images/gun_1.png')
bloodImage = pygame.image.load('assets/images/bloodpatch.png')
gameover = pygame.image.load('assets/images/gameover_1.png')

mainBg = pygame.image.load("assets/images/background_2.png")

def score(hit):
    font_2 = pygame.font.SysFont(None,100)
    text_2 = font_2.render("SCORE : {}".format(str(hit)),True,white)
    font_3 = pygame.font.SysFont(None,25)
    text_3 = font_3.render("Press SPACE to play again...", True,white)
    font_4 = pygame.font.SysFont(None,25)
    text_4 = font_4.render("Press ESC to exit",True,white)
    screen.blit(text_2,(450,570))
    screen.blit(text_3,(490,640))
    screen.blit(text_4,(530,660))

def playscreen():


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()
        screen.blit(playimage, (0, 0))

        pygame.display.update()

def startScreen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.blit(mainBg, (0, 0))

        pygame.display.update()

def bloodPatch(posX, posY):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.blit(bloodImage, (posX-100, posY-100))
        pygame.display.update()
        clock.tick(10)
        break

def timer(s):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Time Left : {0}".format(str(s)), True, red)
    screen.blit(text, (570,70))

def gameOver(hit):

    sound_2.play()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playscreen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        screen.blit(gameover, (0, 0))
        score(hit)


        pygame.display.update()

def game():
    hit = 0
    animalImage = random.choice(animalList)
    animal_x = random.randint(0, width - animalImage.get_width())
    animal_y = random.randint(0, height - animalImage.get_height())
    pygame.time.set_timer(USEREVENT + 1, 1000)
    seconds = 20
    gunY = height - 250

    while True:

        posX, posY = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == USEREVENT + 1:
                seconds -= 1
                # print(seconds)

            if event.type == pygame.MOUSEBUTTONDOWN:
                sound_1.play()
                gunY -= 40
                if gun_rect.colliderect(animal_rect):
                    # pygame.image.load('assets/images/zombie_blood.png')
                    # time.sleep(2)
                    # pygame.time.wait(2000)
                    animalImage = random.choice(animalList)
                    animal_x = random.randint(0, width - animalImage.get_width())
                    animal_y = random.randint(0, height - animalImage.get_height())
                    bloodPatch(posX, posY)
                    hit += 1
            else:
                gunY = height - 250

        screen.fill(blue)
        screen.blit(img_1, (0,0))
        screen.blit(animalImage, (animal_x, animal_y))
        screen.blit(pointer, (posX - 50, posY - 50))
        screen.blit(gunImage, (posX, gunY))

        gun_rect = pygame.Rect(posX - 50, posY - 50, pointer.get_width(), pointer.get_height())
        animal_rect = pygame.Rect(animal_x, animal_y, animalImage.get_width(), animalImage.get_height())

        if seconds == 0:
            gameOver(hit)
            break

        timer(seconds)

        pygame.display.update()
        clock.tick(FPS)


# game()
# startScreen()
playscreen()