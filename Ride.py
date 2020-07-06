import pygame
import random
import sys

def MainMenu():
    pygame.init()
    white = (255,255,255)
    black = (0,0,0)
    width = 1024
    height = 500
    fps = 45
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RIDE")
    font = pygame.font.SysFont('rod', 45)
    title_font = pygame.font.SysFont('arialblack', 72, bold=False)
    bottom_font = pygame.font.SysFont('rod', 24, bold=True)
    bg = pygame.image.load('bg.png')
    sky = pygame.image.load('sky.png')
    sun = pygame.image.load('sun.png')
    horse = pygame.image.load('0.gif')
    start_x = 400
    start_y = 200
    exit_x = 400
    exit_y = 250
    while True:
        clock.tick(fps)
        title_txt = title_font.render('RIDE' , True, black)
        start_txt = font.render('PLAY' , True, white)
        exit_text = font.render('EXIT', True, white)
        bottom_txt = bottom_font.render('This game was inspired by Google Chrome Dinasaur Game', True, white)
        window.blit(sky, (0,0))
        window.blit(sun, (750,30))
        window.blit(bg, (0,280))
        pygame.draw.rect(window ,black ,(start_x,start_y, 200, 40))
        pygame.draw.rect(window ,black ,(exit_x,exit_y, 200, 40))
        window.blit(title_txt, (400, 100))
        window.blit(start_txt, (start_x+50, start_y))
        window.blit(exit_text, (exit_x+50, exit_y))
        window.blit(bottom_txt, (100, 400))
        window.blit(horse, (180,200))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if start_x <= mouse[0] <= start_x+200 and start_y <= mouse[1] <= start_y+200:
                Play()
                break
            if exit_x <= mouse[0] <= exit_x+200 and exit_y <= mouse[1] <= exit_y+200:
                sys.exit()
            

def Play():
    pygame.init()

    #Variables
    white = (255,255,255)
    black = (0,0,0)
    light_blue = (153,217,234)
    width = 1024
    height = 500
    fps = 45
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("RIDE")
    font = pygame.font.SysFont('rod', 28)
    replay_font = pygame.font.SysFont('verdana', 27)
    tip_font = pygame.font.SysFont('courier', 24, bold=True)
    bg = pygame.image.load('bg.png')
    sky = pygame.image.load('sky.png')
    sun = pygame.image.load('sun.png')
    
    obstacles = [pygame.image.load('rock.png'),
                 pygame.image.load('rocks_2.png'),
                 pygame.image.load('rocks_3.png'),
                 pygame.image.load('rocks_4.png'),]


    jumpCount = 0
    peak = 120
    ground = 200
    score = 0
    bg_x = 0
    bg_y = 280
    temp_x = 1024
    temp_y = 230
    vel = 5

    #Classes
    class MainChar(object):
        def __init__(self, x, y, w, h, vel):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.vel = vel
            self.life = 100
            self.index = 0
            self.animation = [pygame.image.load('0.gif'),
                              pygame.image.load('1.gif'),
                              pygame.image.load('2.gif'),
                              pygame.image.load('3.gif'),
                              pygame.image.load('4.gif'),
                              pygame.image.load('5.gif'),]
        def draw(self, screen):
            if not isJump:
                if self.index <= len(self.animation) - 1:
                    screen.blit(self.animation[self.index],(self.x,self.y))
                    self.index += 1
                else:
                    self.index = 0
                    screen.blit(self.animation[self.index],(self.x,self.y))
            else:
                self.index = 5
                screen.blit(self.animation[self.index],(self.x,self.y))

                

    knight = MainChar(180,200,100,90,5)

    temp = random.choice(obstacles)
    def replay_menu(score):
        while True:
            clock.tick(fps)
            score_txt = replay_font.render('Score:   ' + str(score), True, white)
            replay_text = replay_font.render('If you want to replay Press "R"', True, white)
            screen.blit(score_txt, (420, 350))
            screen.blit(replay_text, (300, 390))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                    Play()
                    break


    def drawScreen():
        screen.blit(sky, (0,0))
        screen.blit(sun, (750,30))
        screen.blit(bg, (bg_x,bg_y))
        screen.blit(score_txt, (600, 0))
        if score <= 70:screen.blit(tip_text, (100,100))
        knight.draw(screen)
        screen.blit(temp, (temp_x, temp_y))
        #pygame.draw.rect(screen ,black ,(knight.x,knight.y, knight.w, knight.h),1)
        #pygame.draw.rect(screen ,black ,(temp_x,temp_y, 50, 50),1)
        pygame.display.update()

    #SoundPlay
    #pygame.mixer.music.load('horse-running.wav')
    #pygame.mixer.music.play(30)

    isJump = False
    while True:
        clock.tick(fps)
        score_txt = font.render('Score: '+str(score), True, black)
        tip_text = tip_font.render('Jumpover rocks using UP_ARROW or SPACEBAR', True, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_SPACE]:
                isJump = True
            if keys[pygame.K_DOWN]:
                pass
        #HorseJump
        if isJump == True:
            if jumpCount <= peak:
                jumpCount += knight.vel
                knight.y -= knight.vel
            if jumpCount >= peak and knight.y< ground:
                knight.y += knight.vel
            if knight.y >= ground:
                jumpCount = 0
                isJump = False
        #GroundMotion
        if temp_x >= 0:
            temp_x -= vel
        else:
            temp = random.choice(obstacles)
            temp_x = 1024
            
        if knight.x <= temp_x <= knight.x+knight.w and knight.y <= temp_y <= knight.y+knight.h:
            replay_menu(score)
            break
            
        if bg_x >= -1024:
            bg_x -= vel
        else:
            bg_x = 0
        #ScoreCount
        if score % 500 == 0:
            vel += 1
        score += 1
        drawScreen()
        
    pygame.quit()
MainMenu()
