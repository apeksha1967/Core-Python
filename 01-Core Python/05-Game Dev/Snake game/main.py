import pygame
import random

pygame.init()

blue = 0, 0, 255
red = 255, 0, 0
white = 255, 255, 255
black = 0,0,0

width = 900
height = 600

screen = pygame.display.set_mode((width, height))

sound_1 = pygame.mixer.Sound("assets/music/point.wav")
sound_2 = pygame.mixer.Sound("assets/music/gameover_2.wav")

GameOver = pygame.image.load("assets/images/gameover.png")
playimage = pygame.image.load("assets/images/startscreen.png")
mainBg = pygame.image.load("assets/images/background.png")

fruit_1 = pygame.image.load("assets/images/fruit_1.png")
fruit_2 = pygame.image.load("assets/images/fruit_2.png")
fruit_3 = pygame.image.load("assets/images/fruit_3.png")
fruit_4 = pygame.image.load("assets/images/fruit_4.png")
fruit_5 = pygame.image.load("assets/images/fruit_5.png")
fruit_6 = pygame.image.load("assets/images/fruit_6.png")
fruit_7 = pygame.image.load("assets/images/fruit_7.png")
fruit_8 = pygame.image.load("assets/images/fruit_8.png")

fruitList = [fruit_1,fruit_2,fruit_3,fruit_4,fruit_5,fruit_6,fruit_7,fruit_8]

clock = pygame.time.Clock()

def gameover(counter):
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

        screen.blit(GameOver, (0, 0))
        final(counter)
        pygame.display.update()

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

def score(counter):
    font = pygame.font.SysFont(None, 50)
    text = font.render("Score " + str(counter), True, black)
    screen.blit(text, (420, 25))


def final(counter):
    font_1 = pygame.font.SysFont(None, 70)
    text_1 = font_1.render("SCORE : " + str(counter), True, white)
    font_2 = pygame.font.SysFont(None, 25)
    text_2 = font_2.render("Press SPACE to play again...", True, white)
    font_3 = pygame.font.SysFont(None, 25)
    text_3 = font_3.render("Press ESC to exit", True, white)
    screen.blit(text_1, (315, 360))
    screen.blit(text_2, (321, 410))
    screen.blit(text_3, (360, 435))


def snake(snakeList):
    for s in snakeList:
        pygame.draw.rect(screen, blue, (s[0], s[1], 50, 50))


def game():
    x = 100
    y = 50

    move_x = 0
    move_y = 0

    snake_width = 50
    snakeList = []
    snakeLength = 1

    fruitImage = random.choice(fruitList)
    fruit_x = random.randint(0, width - fruitImage.get_width())
    fruit_y = random.randint(0, height - fruitImage.get_height())

    counter = 0

    FPS = 60
    gameLoop = True

    while gameLoop:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 5
                    move_y = 0
                elif event.key == pygame.K_DOWN:
                    move_y = 5
                    move_x = 0
                elif event.key == pygame.K_LEFT:
                    move_x = -5
                    move_y = 0
                elif event.key == pygame.K_UP:
                    move_y = -5
                    move_x = 0

        screen.fill(white)
        screen.blit(mainBg, (0, 0))
        screen.blit(fruitImage, (fruit_x, fruit_y))

        rect_1 = [x, y, 50, 50]
        # rect_1 = pygame.draw.rect(screen, red, [x, y, snake_width, 50])
        rect_2 = pygame.Rect(fruit_x, fruit_y, fruitImage.get_width(), fruitImage.get_height())

        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)

        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            # print(snakeList)
            del snakeList[0]

        # snakeList[:-1]

        snake(snakeList)

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameover(counter)

        if rect_2.colliderect(rect_1):
            sound_1.play()
            fruitImage = random.choice(fruitList)
            fruit_x = random.randint(0, width - fruitImage.get_width())
            fruit_y = random.randint(0, height - fruitImage.get_height())
            snakeLength += 1
            FPS += 0.5
            counter += 1

        x += move_x
        y += move_y

        if x >= width:
            move_x = -5
        elif x < 0:
            move_x = 5
        elif y >= height:
            move_y = -5
        elif y < 0:
            move_y = 5

        score(counter)

        pygame.display.update()
        clock.tick(FPS)


playscreen()
