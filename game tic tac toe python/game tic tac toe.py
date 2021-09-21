'''
Игра крестики нолики
'''

import pygame
import sys
from fields import Field

FPS = 60

#начало действия игры
pygame.init()

clock = pygame.time.Clock()

#подгрузка картинок х и о
tic =  pygame.Surface((80, 65))
img_x = pygame.image.load('pictures/x.png')
tic.blit(img_x, (0,0))

toe = pygame.Surface((80, 65))
img_o = pygame.image.load('pictures/o.png')
toe.blit(img_o, (0,0))

#подгрузка картинки для меню рестарта
replay_face = pygame.Surface((400, 500))
img_replay = pygame.image.load('pictures/replay_menu.png')
replay_face.blit(img_replay, (0,0))

n = 3

play = 1

while play == 1:
    
    #########  меню
    
    #создание окна для игры
    window = pygame.display.set_mode((520, 510))  #pygame.display-Доступ к дисплею
    
    #создание поля для игры
    screen = pygame.Surface((520, 510))  #pygame.Surface - Управляет изображениями и экраном
        
    #window.fill((200, 200, 200)) #зарисовка окна серым
           
    screen.fill((0, 0, 0))       #зарисовка поля чёрным (RGB)
    
    #для надписи
    myfont = pygame.font.SysFont('monoscpace', 55)  #pygame.font - Использует системные шрифты
    
    ###### с кем играем
    line1 = myfont.render('Game mod', 0, (200, 200, 200))
    line2 = myfont.render('Player vs Player ', 0, (200, 200, 200))
    line3 = myfont.render('Player vs Comp ', 0, (200, 200, 200))
    line4 = myfont.render('Comp vs Comp ', 0, (200, 200, 200))
    
    screen.blit(line1, (120, 80)) #размещение надписи
    screen.blit(line2, (100, 125))
    screen.blit(line3, (100, 170))
    screen.blit(line4, (100, 215))
    
    window.blit(screen, (0, 0)) #размешения поля на экране
    
    pygame.display.update()
    
    act = 1
    while act == 1:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                
                if (x_mouse >= 90 and y_mouse >= 122 and 
                    x_mouse <= 400 and y_mouse <= 167):
                    player1 = 1
                    player2 = 1
                    act = 0
                    break
                
                if (x_mouse >= 90 and y_mouse >= 168 and 
                    x_mouse <= 400 and y_mouse <= 212):
                    player1 = 1
                    player2 = 2
                    act = 0
                    break
                
                if (x_mouse >= 90 and y_mouse >= 213 and 
                    x_mouse <= 400 and y_mouse <= 260):
                    player1 = 2
                    player2 = 2
                    act = 0
                    break
            
                    
    ##### какое поле
    line1 = myfont.render('Which field? ', 0, (200, 200, 200))
    line2 = myfont.render('3x3 ', 0, (200, 200, 200))
    line3 = myfont.render('4x4 ', 0, (200, 200, 200))
    line4 = myfont.render('5x5 ', 0, (200, 200, 200))
    
    screen.fill((0, 0, 0))
    
    screen.blit(line1, (120, 80)) #размещение надписи
    screen.blit(line2, (170, 125))
    screen.blit(line3, (170, 170))
    screen.blit(line4, (170, 215))
    
    window.blit(screen, (0, 0))
    
    pygame.display.update()
    
    
    act = 1
    while act == 1:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                
                if (x_mouse >= 90 and y_mouse >= 122 and 
                    x_mouse <= 400 and y_mouse <= 167):
                    n = 3
                    field = Field(n, player1, player2)
                    act = 0
                    break
                
                if (x_mouse >= 90 and y_mouse >= 168 and 
                    x_mouse <= 400 and y_mouse <= 212):
                    n = 4
                    field = Field(n, player1, player2)
                    act = 0
                    break
                
                if (x_mouse >= 90 and y_mouse >= 213 and 
                    x_mouse <= 400 and y_mouse <= 260):
                    n = 5
                    field = Field(n, player1, player2)
                    act = 0
                    break
    
    
    ##########  сама игра
    
    replay = 0
    stop = 0
    win = 0
    
    #повтор игры
    while stop == 0:
        
        
        screen.fill((0, 0, 0))
        screen.blit(field.field_face, (0, 0))
        window.fill((200, 200, 200)) #серую полоску добавляю, для записей, кто играет  
        window.blit(screen, (0, 70))
    
        pygame.display.update()
        
    
        #ход игры 
        move = 0
        while move < n**2:
            
            
            #для смены хода играков
            moves_detector = replay % 2
            
            #ход первого инрока
            if move % 2 == moves_detector:
                name1 = myfont.render('Player1', 0, (200, 0, 0))
                name2 = myfont.render('Player2', 0, (100, 0, 0))
                window.blit(name1, (20, 20))
                window.blit(name2, (250, 20))
                pygame.display.update()
                
                #pas - преймущество
                if moves_detector == 0:
                    pas = 1
                else:
                    pas = 2
                    
                screen.blit(tic, field.move(1, pas, move))
                
                #проверка победы
                if move >= 2*n - 2:
                    if field.win(1):
                        win = 1
                    
            #ход второго игрока
            if  move % 2 != moves_detector:
                name1 = myfont.render('Player1', 0, (100, 0, 0))
                name2 = myfont.render('Player2', 0, (200, 0, 0))
                window.blit(name1, (20, 20))
                window.blit(name2, (250, 20))
                pygame.display.update()
                
                if moves_detector == 1:
                    pas = 1
                else:
                    pas = 2
                    
                screen.blit(toe, field.move(2, pas, move))
                
                #проверка победы
                if move >= 2*n - 2:
                    if field.win(2):
                        win = 2
            
            
            window.blit(screen, (0, 70))
            pygame.display.update()
            
            if win > 0:
                break
            
            move+=1
        
        #конец игры
        window.fill((0, 0, 0))
        
        #кто победил
        if win == 1:
            line = myfont.render('Win Player1', 0, (200, 200, 200))
        if win == 2:
            line = myfont.render('Win Player2', 0, (200, 200, 200))
        if win == 0:
            line = myfont.render('Draw', 0, (200, 200, 200))
        
        win = 0
        
        #меню рестарта
       
        window.blit(line, (20, 20))
        window.blit(replay_face, (300, 5))
        window.blit(screen, (0, 70)) 
         
        pygame.display.update()
        
        act = 1
        while act == 1:
            clock.tick(FPS)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    #print(x_mouse, y_mouse)
                
                    if (x_mouse >= 310 and y_mouse >= 10 and 
                        x_mouse <= 385 and y_mouse <= 70):
                        replay += 1
                        field.to_empty()
                        act = 0
                        break
                
                    if (x_mouse >= 415 and y_mouse >= 15 and 
                        x_mouse <= 490 and y_mouse <= 45):
                        stop = 1
                        act = 0
                        break
    
    

    
#конец игры
pygame.quit()
    
