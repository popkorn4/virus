from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.ttk import Radiobutton
import sys
import pygame
for i in range(30):
    def clicked1():
        def main():
            display = tk.Tk()
            log_pass(display)
            display.mainloop()

        def log_pass(okno):
            login = tk.Entry(okno)
            login.grid(row=0, column=0)

            password = tk.Entry(okno)
            password.grid(row=1, column=0)
            check_btn = ttk.Button(okno, text="Войти", command=lambda: get_key(login.get(), password.get()))
            check_btn.grid(row=2, column=0)

        def get_key(login, password):
            if login == 'codabra' and password == 'qwerty':
                print('okey')
                mem_window()

        def mem_window():
            mem_display = tk.Toplevel()
            img = Image.open("music/" + f"123.png")
            img = ImageTk.PhotoImage(img)

            picture = tk.Label(mem_display, image=img)
            picture.grid(row=0, column=0)
            mem_display.mainloop()
            sys.exit()

        if __name__ == "__main__":
            main()


    def clicked2():
        import pygame, sys, random

        Display = pygame.display.set_mode((640, 400))  # размер от 640 до 400
        pygame.display.set_caption("SNIPER ELITE 3000")

        target = pygame.image.load("cherep.jpg")
        targetPosition = target.get_rect()
        targetPosition.bottom = random.randint(32, 368)
        targetPosition.left = random.randint(0, 592)
        pygame.mixer.init()
        tracks = ['music/dance.mp3', 'music/song.mp3', 'music/tiger.ogg']
        pygame.mixer.music.load(random.choice(tracks))
        # pygame.mixer.music.play()
        # pygame.mixer.music.set_volume(0.1)
        while True:
            pygame.mouse.set_visible(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    #sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        shot = pygame.Rect(x, y, 1, 1)
                        if shot.colliderect(targetPosition):
                            targetPosition.bottom = random.randint(32, 368)
                            targetPosition.left = random.randint(0, 592)
                        shoutSound = pygame.mixer.Sound("weapons/laser1.wav")
                        shoutSound.play()
            Display.fill((0, 0, 0))
            Display.blit(target, targetPosition)
            pygame.draw.line(Display, (255, 255, 255), (0, y), (640, y))
            pygame.draw.line(Display, (255, 255, 255), (x, 0), (x, 400))
            pygame.display.update()

            pygame.mixer.init()
            pygame.mixer.music.load('Frank Sinatra - New York, New York (www.hotplayer.ru).mp3')
            pygame.mixer.music.play(loops=-1)



    def clicked3():
        import pygame, sys, random
        SIZE_A = 30
        SIZE_B = 90
        H = 1000  # размер окна в высоту
        W = 1400  # розмер окна в ширину
        Display = pygame.display.set_mode((W, H))
        FPS = 30
        fpsClock = pygame.time.Clock()

        def finish():
            pygame.quit()
            #sys.exit(0)

        def main():
            pygame.mixer.init()
            pygame.mixer.music.load('Frank Sinatra - New York, New York (www.hotplayer.ru).mp3')
            pygame.mixer.music.play()
            hero = pygame.Rect(W / 2, H - 40, SIZE_B, SIZE_A)
            enemy = pygame.Rect(W / 2, 40, SIZE_B, SIZE_A)
            ball = pygame.Rect(W / 2, H / 2, 18, 18)
            x_ball_speed = 0
            y_ball_speed = 0
            while not x_ball_speed:
                x_ball_speed = 4
            while not y_ball_speed:
                y_ball_speed = -4
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finish()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    hero.move_ip(-15, 0)
                elif keys[pygame.K_RIGHT]:
                    hero.move_ip(15, 0)
                if keys[pygame.K_d]:
                    enemy.move_ip(15, 0)
                elif keys[pygame.K_a]:
                    enemy.move_ip(-15, 0)
                ball.move_ip(x_ball_speed, y_ball_speed)
                if ball.x > W - 15:
                    x_ball_speed = -10
                if ball.x < 0:
                    x_ball_speed = 10
                if ball.y > H:
                    return
                if ball.y < - 15:
                    return
                if ball.colliderect(enemy):
                    y_ball_speed = 10
                if ball.colliderect(hero):
                    y_ball_speed = -10
                Display.fill((19, 218, 232))
                pygame.draw.rect(Display, (255, 0, 0), hero)
                pygame.draw.rect(Display, (0, 0, 0), ball)
                pygame.draw.rect(Display, (0, 0, 255), enemy)
                pygame.display.update()
                fpsClock.tick(FPS)

        main()
        finish()


    def clicked4():
        import pygame
        import time
        import random

        pygame.init()

        white = (255, 255, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        window_width = 800
        window_height = 600

        gameDisplay = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption('slither')

        clock = pygame.time.Clock()
        FPS = 20
        blockSize = 15
        noPixel = 0

        font = pygame.font.SysFont(None, 25, bold=True)

        def snake(blockSize, snakelist):
            for size in snakelist:
                pygame.draw.rect(gameDisplay, black, [size[0], size[1], blockSize, blockSize])

        def message_to_screen(msg, color):
            screen_text = font.render(msg, True, color)
            gameDisplay.blit(screen_text, [window_width / 2, window_height / 2])

        def gameLoop():
            gameExit = False
            gameOver = False

            lead_x = window_width / 2
            lead_y = window_height / 2

            change_pixels_of_x = 0
            change_pixels_of_y = 0

            snakelist = []
            snakeLength = 1

            randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0
            randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0

            while not gameExit:

                while gameOver == True:
                    gameDisplay.fill(white)
                    message_to_screen("Game over, press c to play again or Q to quit", red)
                    pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameOver = False
                            gameExit = True

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                gameExit = True
                                gameOver = False
                            if event.key == pygame.K_c:
                                gameLoop()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True

                    if event.type == pygame.KEYDOWN:

                        leftArrow = event.key == pygame.K_LEFT
                        rightArrow = event.key == pygame.K_RIGHT
                        upArrow = event.key == pygame.K_UP
                        downArrow = event.key == pygame.K_DOWN

                        if leftArrow:
                            change_pixels_of_x = -blockSize
                            change_pixels_of_y = noPixel
                        elif rightArrow:
                            change_pixels_of_x = blockSize
                            change_pixels_of_y = noPixel
                        elif upArrow:
                            change_pixels_of_y = -blockSize
                            change_pixels_of_x = noPixel
                        elif downArrow:
                            change_pixels_of_y = blockSize
                            change_pixels_of_x = noPixel

                    if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                        gameOver = True

                lead_x += change_pixels_of_x
                lead_y += change_pixels_of_y

                gameDisplay.fill(white)

                AppleThickness = 10
                pygame.draw.rect(gameDisplay, red, [randomAppleX, randomAppleY, AppleThickness, AppleThickness])

                snakehead = []
                snakehead.append(lead_x)
                snakehead.append(lead_y)
                snakelist.append(snakehead)

                if len(snakelist) > snakeLength:
                    del snakelist[0]

                for eachSegment in snakelist[:-1]:
                    if eachSegment == snakehead:
                        gameOver = True

                snake(blockSize, snakelist)

                pygame.display.update()

                if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
                    if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                        randomAppleX = round(random.randrange(0, window_width - blockSize) / 10.0) * 10.0
                        randomAppleY = round(random.randrange(0, window_height - blockSize) / 10.0) * 10.0
                        snakeLength += 1

                clock.tick(FPS)

            pygame.quit()


        gameLoop()


    def clicked5():
        import pygame
        import sys
        import random
        SIZE_A = 19.5
        SIZE_B = 100
        SIZE_C = 49.5
        SIZE_D = 1
        H = 800  # размер окна в высоту
        W = 1000  # розмер окна в ширину
        Display = pygame.display.set_mode((W, H))
        FPS = 40
        fpsClock = pygame.time.Clock()

        def finish():
            pygame.quit()

        def main():

            hero = pygame.Rect(W / 2, H - 40, SIZE_B, SIZE_A)
            line = pygame.Rect(0, 1, 3000, SIZE_D)
            enemy1 = pygame.Rect(0, 81, SIZE_C, SIZE_A)
            enemy2 = pygame.Rect(50, 81, SIZE_C, SIZE_A)
            enemy3 = pygame.Rect(100, 81, SIZE_C, SIZE_A)
            enemy4 = pygame.Rect(150, 81, SIZE_C, SIZE_A)
            enemy5 = pygame.Rect(200, 81, SIZE_C, SIZE_A)
            enemy6 = pygame.Rect(250, 81, SIZE_C, SIZE_A)
            enemy7 = pygame.Rect(300, 81, SIZE_C, SIZE_A)
            enemy8 = pygame.Rect(350, 81, SIZE_C, SIZE_A)
            enemy9 = pygame.Rect(400, 81, SIZE_C, SIZE_A)
            enemy10 = pygame.Rect(450, 81, SIZE_C, SIZE_A)
            enemy = pygame.Rect(W / 2, 81, SIZE_C, SIZE_A)
            enemy12 = pygame.Rect(550, 81, SIZE_C, SIZE_A)
            enemy13 = pygame.Rect(600, 81, SIZE_C, SIZE_A)
            enemy14 = pygame.Rect(650, 81, SIZE_C, SIZE_A)
            enemy15 = pygame.Rect(700, 81, SIZE_C, SIZE_A)
            enemy16 = pygame.Rect(750, 81, SIZE_C, SIZE_A)
            enemy17 = pygame.Rect(800, 81, SIZE_C, SIZE_A)
            enemy18 = pygame.Rect(850, 81, SIZE_C, SIZE_A)
            enemy19 = pygame.Rect(900, 81, SIZE_C, SIZE_A)
            enemy20 = pygame.Rect(950, 81, SIZE_C, SIZE_A)
            enemy21 = pygame.Rect(1000, 81, SIZE_C, SIZE_A)
            enemy1t = pygame.Rect(0, 21, SIZE_C, SIZE_A)
            enemy2t = pygame.Rect(50, 21, SIZE_C, SIZE_A)
            enemy3t = pygame.Rect(100, 21, SIZE_C, SIZE_A)
            enemy4t = pygame.Rect(150, 21, SIZE_C, SIZE_A)
            enemy5t = pygame.Rect(200, 21, SIZE_C, SIZE_A)
            enemy6t = pygame.Rect(250, 21, SIZE_C, SIZE_A)
            enemy7t = pygame.Rect(300, 21, SIZE_C, SIZE_A)
            enemy8t = pygame.Rect(350, 21, SIZE_C, SIZE_A)
            enemy9t = pygame.Rect(400, 21, SIZE_C, SIZE_A)
            enemy10t = pygame.Rect(450, 21, SIZE_C, SIZE_A)
            enemyt = pygame.Rect(W / 2, 21, SIZE_C, SIZE_A)
            enemy12t = pygame.Rect(550, 21, SIZE_C, SIZE_A)
            enemy13t = pygame.Rect(600, 21, SIZE_C, SIZE_A)
            enemy14t = pygame.Rect(650, 21, SIZE_C, SIZE_A)
            enemy15t = pygame.Rect(700, 21, SIZE_C, SIZE_A)
            enemy16t = pygame.Rect(750, 21, SIZE_C, SIZE_A)
            enemy17t = pygame.Rect(800, 21, SIZE_C, SIZE_A)
            enemy18t = pygame.Rect(850, 21, SIZE_C, SIZE_A)
            enemy19t = pygame.Rect(900, 21, SIZE_C, SIZE_A)
            enemy20t = pygame.Rect(950, 21, SIZE_C, SIZE_A)
            enemy21t = pygame.Rect(1000, 21, SIZE_C, SIZE_A)
            enemy1g = pygame.Rect(0, 41, SIZE_C, SIZE_A)
            enemy2g = pygame.Rect(50, 41, SIZE_C, SIZE_A)
            enemy3g = pygame.Rect(100, 41, SIZE_C, SIZE_A)
            enemy4g = pygame.Rect(150, 41, SIZE_C, SIZE_A)
            enemy5g = pygame.Rect(200, 41, SIZE_C, SIZE_A)
            enemy6g = pygame.Rect(250, 41, SIZE_C, SIZE_A)
            enemy7g = pygame.Rect(300, 41, SIZE_C, SIZE_A)
            enemy8g = pygame.Rect(350, 41, SIZE_C, SIZE_A)
            enemy9g = pygame.Rect(400, 41, SIZE_C, SIZE_A)
            enemy10g = pygame.Rect(450, 41, SIZE_C, SIZE_A)
            enemyg = pygame.Rect(W / 2, 41, SIZE_C, SIZE_A)
            enemy12g = pygame.Rect(550, 41, SIZE_C, SIZE_A)
            enemy13g = pygame.Rect(600, 41, SIZE_C, SIZE_A)
            enemy14g = pygame.Rect(650, 41, SIZE_C, SIZE_A)
            enemy15g = pygame.Rect(700, 41, SIZE_C, SIZE_A)
            enemy16g = pygame.Rect(750, 41, SIZE_C, SIZE_A)
            enemy17g = pygame.Rect(800, 41, SIZE_C, SIZE_A)
            enemy18g = pygame.Rect(850, 41, SIZE_C, SIZE_A)
            enemy19g = pygame.Rect(900, 41, SIZE_C, SIZE_A)
            enemy20g = pygame.Rect(950, 41, SIZE_C, SIZE_A)
            enemy21g = pygame.Rect(1000, 41, SIZE_C, SIZE_A)
            enemy1h = pygame.Rect(0, 61, SIZE_C, SIZE_A)
            enemy2h = pygame.Rect(50, 61, SIZE_C, SIZE_A)
            enemy3h = pygame.Rect(100, 61, SIZE_C, SIZE_A)
            enemy4h = pygame.Rect(150, 61, SIZE_C, SIZE_A)
            enemy5h = pygame.Rect(200, 61, SIZE_C, SIZE_A)
            enemy6h = pygame.Rect(250, 61, SIZE_C, SIZE_A)
            enemy7h = pygame.Rect(300, 61, SIZE_C, SIZE_A)
            enemy8h = pygame.Rect(350, 61, SIZE_C, SIZE_A)
            enemy9h = pygame.Rect(400, 61, SIZE_C, SIZE_A)
            enemy10h = pygame.Rect(450, 61, SIZE_C, SIZE_A)
            enemyh = pygame.Rect(W / 2, 61, SIZE_C, SIZE_A)
            enemy12h = pygame.Rect(550, 61, SIZE_C, SIZE_A)
            enemy13h = pygame.Rect(600, 61, SIZE_C, SIZE_A)
            enemy14h = pygame.Rect(650, 61, SIZE_C, SIZE_A)
            enemy15h = pygame.Rect(700, 61, SIZE_C, SIZE_A)
            enemy16h = pygame.Rect(750, 61, SIZE_C, SIZE_A)
            enemy17h = pygame.Rect(800, 61, SIZE_C, SIZE_A)
            enemy18h = pygame.Rect(850, 61, SIZE_C, SIZE_A)
            enemy19h = pygame.Rect(900, 61, SIZE_C, SIZE_A)
            enemy20h = pygame.Rect(950, 61, SIZE_C, SIZE_A)
            enemy21h = pygame.Rect(1000, 61, SIZE_C, SIZE_A)
            enemy1q = pygame.Rect(0, 101, SIZE_C, SIZE_A)
            enemy2q = pygame.Rect(50, 101, SIZE_C, SIZE_A)
            enemy3q = pygame.Rect(100, 101, SIZE_C, SIZE_A)
            enemy4q = pygame.Rect(150, 101, SIZE_C, SIZE_A)
            enemy5q = pygame.Rect(200, 101, SIZE_C, SIZE_A)
            enemy6q = pygame.Rect(250, 101, SIZE_C, SIZE_A)
            enemy7q = pygame.Rect(300, 101, SIZE_C, SIZE_A)
            enemy8q = pygame.Rect(350, 101, SIZE_C, SIZE_A)
            enemy9q = pygame.Rect(400, 101, SIZE_C, SIZE_A)
            enemy10q = pygame.Rect(450, 101, SIZE_C, SIZE_A)
            enemyq = pygame.Rect(W / 2, 101, SIZE_C, SIZE_A)
            enemy12q = pygame.Rect(550, 101, SIZE_C, SIZE_A)
            enemy13q = pygame.Rect(600, 101, SIZE_C, SIZE_A)
            enemy14q = pygame.Rect(650, 101, SIZE_C, SIZE_A)
            enemy15q = pygame.Rect(700, 101, SIZE_C, SIZE_A)
            enemy16q = pygame.Rect(750, 101, SIZE_C, SIZE_A)
            enemy17q = pygame.Rect(800, 101, SIZE_C, SIZE_A)
            enemy18q = pygame.Rect(850, 101, SIZE_C, SIZE_A)
            enemy19q = pygame.Rect(900, 101, SIZE_C, SIZE_A)
            enemy20q = pygame.Rect(950, 101, SIZE_C, SIZE_A)
            enemy21q = pygame.Rect(1000, 101, SIZE_C, SIZE_A)

            ball = pygame.Rect(W / 2, H / 2, 13, 13)
            x_ball_speed = 0
            y_ball_speed = 0
            while not x_ball_speed:
                x_ball_speed = 4
            while not y_ball_speed:
                y_ball_speed = -4
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finish()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    hero.move_ip(-15, 0)
                elif keys[pygame.K_RIGHT]:
                    hero.move_ip(15, 0)
                ball.move_ip(x_ball_speed, y_ball_speed)
                if ball.x > W - 15:
                    x_ball_speed = -10
                if ball.x < 0:
                    x_ball_speed = 10
                if ball.y > H:
                    return
                if ball.y < - 15:
                    return
                if ball.colliderect(enemy):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy):
                    enemy = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy1):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy1):
                    enemy1 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy2):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy2):
                    enemy2 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy3):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy3):
                    enemy3 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy4):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy4):
                    enemy4 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy5):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy5):
                    enemy5 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy6):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy6):
                    enemy6 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy7):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy7):
                    enemy7 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy8):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy8):
                    enemy8 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy9):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy9):
                    enemy9 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy10):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy10):
                    enemy10 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy12):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy12):
                    enemy12 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy13):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy13):
                    enemy13 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy14):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy14):
                    enemy14 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy15):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy15):
                    enemy15 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy16):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy16):
                    enemy16 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy17):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy17):
                    enemy17 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy18):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy18):
                    enemy18 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy19):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy19):
                    enemy19 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy20):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy20):
                    enemy20 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy21):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy21):
                    enemy21 = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemyt):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemyt):
                    enemyt = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy1t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy1t):
                    enemy1t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy2t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy2t):
                    enemy2t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy3t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy3t):
                    enemy3t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy4t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy4t):
                    enemy4t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy5t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy5t):
                    enemy5t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy6t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy6t):
                    enemy6t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy7t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy7t):
                    enemy7t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy8t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy8t):
                    enemy8t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy9t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy9t):
                    enemy9t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy10t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy10t):
                    enemy10t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy12t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy12t):
                    enemy12t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy13t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy13t):
                    enemy13t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy14t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy14t):
                    enemy14t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy15t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy15t):
                    enemy15t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy16t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy16t):
                    enemy16t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy17t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy17t):
                    enemy17t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy18t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy18t):
                    enemy18t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy19t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy19t):
                    enemy19t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy20t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy20t):
                    enemy20t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy21t):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy21t):
                    enemy21t = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(hero):
                    y_ball_speed = -10
                if ball.colliderect(line):
                    y_ball_speed = 10
                if ball.colliderect(enemyg):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemyg):
                    enemyg = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy1g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy1g):
                    enemy1g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy2g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy2g):
                    enemy2g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy3g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy3g):
                    enemy3g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy4g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy4g):
                    enemy4g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy5g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy5g):
                    enemy5g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy6g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy6g):
                    enemy6g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy7g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy7g):
                    enemy7g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy8g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy8g):
                    enemy8g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy9g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy9g):
                    enemy9g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy10g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy10g):
                    enemy10g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy12g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy12g):
                    enemy12g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy13g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy13g):
                    enemy13g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy14g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy14g):
                    enemy14g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy15g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy15g):
                    enemy15g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy16g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy16g):
                    enemy16g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy17g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy17g):
                    enemy17g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy18g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy18g):
                    enemy18g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy19g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy19g):
                    enemy19g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy20g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy20g):
                    enemy20g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy21g):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy21g):
                    enemy21g = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemyh):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemyh):
                    enemyh = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy1h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy1h):
                    enemy1h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy2h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy2h):
                    enemy2h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy3h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy3h):
                    enemy3h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy4h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy4h):
                    enemy4h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy5h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy5h):
                    enemy5h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy6h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy6h):
                    enemy6h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy7h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy7h):
                    enemy7h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy8h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy8h):
                    enemy8h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy9h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy9h):
                    enemy9h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy10h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy10h):
                    enemy10h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy12h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy12h):
                    enemy12h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy13h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy13h):
                    enemy13h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy14h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy14h):
                    enemy14h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy15h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy15h):
                    enemy15h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy16h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy16h):
                    enemy16h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy17h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy17h):
                    enemy17h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy18h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy18h):
                    enemy18h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy19h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy19h):
                    enemy19h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy20h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy20h):
                    enemy20h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy21h):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy21h):
                    enemy21h = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemyq):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemyq):
                    enemyq = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy1q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy1q):
                    enemy1q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy2q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy2q):
                    enemy2q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy3q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy3q):
                    enemy3q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy4q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy4q):
                    enemy4q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy5q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy5q):
                    enemy5q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy6q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy6q):
                    enemy6q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy7q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy7q):
                    enemy7q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy8q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy8q):
                    enemy8q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy9q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy9q):
                    enemy9q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy10q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy10q):
                    enemy10q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy12q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy12q):
                    enemy12q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy13q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy13q):
                    enemy13q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy14q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy14q):
                    enemy14q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy15q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy15q):
                    enemy15q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy16q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy16q):
                    enemy16q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy17q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy17q):
                    enemy17q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy18q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy18q):
                    enemy18q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy19q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy19q):
                    enemy19q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy20q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy20q):
                    enemy20q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                if ball.colliderect(enemy21q):
                    y_ball_speed = -y_ball_speed
                if ball.colliderect(enemy21q):
                    enemy21q = pygame.Rect(1500, 1500, SIZE_C, SIZE_A)
                Display.fill((0, 0, 0))
                pygame.draw.rect(Display, (255, 0, 0), hero)
                pygame.draw.rect(Display, (0, 0, 255), ball)
                pygame.draw.rect(Display, (0, 255, 0), enemy)
                pygame.draw.rect(Display, (0, 255, 0), enemy1)
                pygame.draw.rect(Display, (0, 255, 0), enemy2)
                pygame.draw.rect(Display, (0, 255, 0), enemy3)
                pygame.draw.rect(Display, (0, 255, 0), enemy4)
                pygame.draw.rect(Display, (0, 255, 0), enemy5)
                pygame.draw.rect(Display, (0, 255, 0), enemy6)
                pygame.draw.rect(Display, (0, 255, 0), enemy7)
                pygame.draw.rect(Display, (0, 255, 0), enemy8)
                pygame.draw.rect(Display, (0, 255, 0), enemy9)
                pygame.draw.rect(Display, (0, 255, 0), enemy10)
                pygame.draw.rect(Display, (0, 255, 0), enemy12)
                pygame.draw.rect(Display, (0, 255, 0), enemy13)
                pygame.draw.rect(Display, (0, 255, 0), enemy14)
                pygame.draw.rect(Display, (0, 255, 0), enemy15)
                pygame.draw.rect(Display, (0, 255, 0), enemy16)
                pygame.draw.rect(Display, (0, 255, 0), enemy17)
                pygame.draw.rect(Display, (0, 255, 0), enemy18)
                pygame.draw.rect(Display, (0, 255, 0), enemy19)
                pygame.draw.rect(Display, (0, 255, 0), enemy20)
                pygame.draw.rect(Display, (0, 255, 0), enemy21)
                pygame.draw.rect(Display, (0, 255, 0), enemyt)
                pygame.draw.rect(Display, (0, 255, 0), enemy1t)
                pygame.draw.rect(Display, (0, 255, 0), enemy2t)
                pygame.draw.rect(Display, (0, 255, 0), enemy3t)
                pygame.draw.rect(Display, (0, 255, 0), enemy4t)
                pygame.draw.rect(Display, (0, 255, 0), enemy5t)
                pygame.draw.rect(Display, (0, 255, 0), enemy6t)
                pygame.draw.rect(Display, (0, 255, 0), enemy7t)
                pygame.draw.rect(Display, (0, 255, 0), enemy8t)
                pygame.draw.rect(Display, (0, 255, 0), enemy9t)
                pygame.draw.rect(Display, (0, 255, 0), enemy10t)
                pygame.draw.rect(Display, (0, 255, 0), enemy12t)
                pygame.draw.rect(Display, (0, 255, 0), enemy13t)
                pygame.draw.rect(Display, (0, 255, 0), enemy14t)
                pygame.draw.rect(Display, (0, 255, 0), enemy15t)
                pygame.draw.rect(Display, (0, 255, 0), enemy16t)
                pygame.draw.rect(Display, (0, 255, 0), enemy17t)
                pygame.draw.rect(Display, (0, 255, 0), enemy18t)
                pygame.draw.rect(Display, (0, 255, 0), enemy19t)
                pygame.draw.rect(Display, (0, 255, 0), enemy20t)
                pygame.draw.rect(Display, (0, 255, 0), enemy21t)
                pygame.draw.rect(Display, (0, 255, 0), enemyg)
                pygame.draw.rect(Display, (0, 255, 0), enemy1g)
                pygame.draw.rect(Display, (0, 255, 0), enemy2g)
                pygame.draw.rect(Display, (0, 255, 0), enemy3g)
                pygame.draw.rect(Display, (0, 255, 0), enemy4g)
                pygame.draw.rect(Display, (0, 255, 0), enemy5g)
                pygame.draw.rect(Display, (0, 255, 0), enemy6g)
                pygame.draw.rect(Display, (0, 255, 0), enemy7g)
                pygame.draw.rect(Display, (0, 255, 0), enemy8g)
                pygame.draw.rect(Display, (0, 255, 0), enemy9g)
                pygame.draw.rect(Display, (0, 255, 0), enemy10g)
                pygame.draw.rect(Display, (0, 255, 0), enemy12g)
                pygame.draw.rect(Display, (0, 255, 0), enemy13g)
                pygame.draw.rect(Display, (0, 255, 0), enemy14g)
                pygame.draw.rect(Display, (0, 255, 0), enemy15g)
                pygame.draw.rect(Display, (0, 255, 0), enemy16g)
                pygame.draw.rect(Display, (0, 255, 0), enemy17g)
                pygame.draw.rect(Display, (0, 255, 0), enemy18g)
                pygame.draw.rect(Display, (0, 255, 0), enemy19g)
                pygame.draw.rect(Display, (0, 255, 0), enemy20g)
                pygame.draw.rect(Display, (0, 255, 0), enemy21g)
                pygame.draw.rect(Display, (0, 255, 0), enemyh)
                pygame.draw.rect(Display, (0, 255, 0), enemy1h)
                pygame.draw.rect(Display, (0, 255, 0), enemy2h)
                pygame.draw.rect(Display, (0, 255, 0), enemy3h)
                pygame.draw.rect(Display, (0, 255, 0), enemy4h)
                pygame.draw.rect(Display, (0, 255, 0), enemy5h)
                pygame.draw.rect(Display, (0, 255, 0), enemy6h)
                pygame.draw.rect(Display, (0, 255, 0), enemy7h)
                pygame.draw.rect(Display, (0, 255, 0), enemy8h)
                pygame.draw.rect(Display, (0, 255, 0), enemy9h)
                pygame.draw.rect(Display, (0, 255, 0), enemy10h)
                pygame.draw.rect(Display, (0, 255, 0), enemy12h)
                pygame.draw.rect(Display, (0, 255, 0), enemy13h)
                pygame.draw.rect(Display, (0, 255, 0), enemy14h)
                pygame.draw.rect(Display, (0, 255, 0), enemy15h)
                pygame.draw.rect(Display, (0, 255, 0), enemy16h)
                pygame.draw.rect(Display, (0, 255, 0), enemy17h)
                pygame.draw.rect(Display, (0, 255, 0), enemy18h)
                pygame.draw.rect(Display, (0, 255, 0), enemy19h)
                pygame.draw.rect(Display, (0, 255, 0), enemy20h)
                pygame.draw.rect(Display, (0, 255, 0), enemy21h)
                pygame.draw.rect(Display, (0, 255, 0), enemyq)
                pygame.draw.rect(Display, (0, 255, 0), enemy1q)
                pygame.draw.rect(Display, (0, 255, 0), enemy2q)
                pygame.draw.rect(Display, (0, 255, 0), enemy3q)
                pygame.draw.rect(Display, (0, 255, 0), enemy4q)
                pygame.draw.rect(Display, (0, 255, 0), enemy5q)
                pygame.draw.rect(Display, (0, 255, 0), enemy6q)
                pygame.draw.rect(Display, (0, 255, 0), enemy7q)
                pygame.draw.rect(Display, (0, 255, 0), enemy8q)
                pygame.draw.rect(Display, (0, 255, 0), enemy9q)
                pygame.draw.rect(Display, (0, 255, 0), enemy10q)
                pygame.draw.rect(Display, (0, 255, 0), enemy12q)
                pygame.draw.rect(Display, (0, 255, 0), enemy13q)
                pygame.draw.rect(Display, (0, 255, 0), enemy14q)
                pygame.draw.rect(Display, (0, 255, 0), enemy15q)
                pygame.draw.rect(Display, (0, 255, 0), enemy16q)
                pygame.draw.rect(Display, (0, 255, 0), enemy17q)
                pygame.draw.rect(Display, (0, 255, 0), enemy18q)
                pygame.draw.rect(Display, (0, 255, 0), enemy19q)
                pygame.draw.rect(Display, (0, 255, 0), enemy20q)
                pygame.draw.rect(Display, (0, 255, 0), enemy21q)
                pygame.draw.rect(Display, (0, 255, 0), line)
                pygame.display.update()
                fpsClock.tick(FPS)

        main()
        finish()


    window = Tk()
    window.title("это вирус")
    window.geometry('3840x2140')
    lbl = Label(window, text="Привет я вирус", font=("Arial Bold", 130))
    lbl.grid(column=0, row=0)
    rad1 = Radiobutton(window, text='Первый', value=1, command=clicked1)
    rad2 = Radiobutton(window, text='Второй', value=2, command=clicked2)
    rad3 = Radiobutton(window, text='Третий', value=3, command=clicked3)
    rad4 = Radiobutton(window, text='Четёртый', value=4, command=clicked4)
    rad5= Radiobutton(window, text='Пятый', value=5, command=clicked5)
    rad1.grid(column=1, row=0)
    rad2.grid(column=2, row=0)
    rad3.grid(column=3, row=0)
    rad4.grid(column=1, row=1)
    rad5.grid(column=2, row=1)
    window.mainloop()