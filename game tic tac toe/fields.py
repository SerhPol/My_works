'''
Поля для игры в крестики нолики
распознование хода человека
расчет хода компьютера
проверка победы

запись клеток ведется в двойных массивах 
и начинаются от 1
пример
[1,1] [1,2] [1,3]
[2,1] [2,2] [2,3]
[3,1] [3,2] [3,3]
'''

import pygame
import sys
import random
import time

FPS = 60
clock = pygame.time.Clock()


#для поля 3*3
class Three:
    def __init__(self):
        self.n = 3
        self.img = pygame.image.load('pictures/field_3.png')
        
    #получение координат
    def getCoordinate(self, c):
        if c == [1, 1]:
            return (60, 75)
        if c == [1, 2]:
            return (220, 75)
        if c == [1, 3] :
            return (375, 75) 
        if c == [2, 1]:
            return (60, 190)
        if c == [2, 2]:
            return (220, 190)
        if c == [2, 3]:
            return (375, 195)
        if c == [3, 1]:
            return (60, 300)
        if c == [3, 2]:
            return (210, 300)
        if c == [3, 3]:
            return (370, 305)
    
        
    #для хода игрока на поле 3*3
    def humanMove(self, my_moves, other_moves):
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
                    
                    #первый ряд
                    if (x_mouse >= 30 and y_mouse >= 120 and 
                        x_mouse <= 175 and y_mouse <= 230):
                        if [1, 1] not in my_moves and [1, 1] not in other_moves:
                            return [1, 1]
                    
                    if (x_mouse >= 185 and y_mouse >= 120 and 
                        x_mouse <= 330 and y_mouse <= 230):
                        if [1, 2] not in my_moves and [1, 2] not in other_moves:
                            return [1, 2]
                    
                    if (x_mouse >= 335 and y_mouse >= 120 and 
                        x_mouse <= 485 and y_mouse <= 230):
                        if [1, 3] not in my_moves and [1, 3] not in other_moves:
                            return [1, 3] 
                    
                    #второй ряд
                    
                    
                    if (x_mouse >= 30 and y_mouse >= 235 and 
                        x_mouse <= 175 and y_mouse <= 345):
                        if [2, 1] not in my_moves and [2, 1] not in other_moves:
                            return [2, 1]
                        
                    if (x_mouse >= 185 and y_mouse >= 235 and 
                        x_mouse <= 330 and y_mouse <= 345):
                        if [2, 2] not in my_moves and [2, 2] not in other_moves:
                            return [2, 2]
                    
                    if (x_mouse >= 335 and y_mouse >= 235 and 
                        x_mouse <= 485 and y_mouse <= 345):
                        if [2, 3] not in my_moves and [2, 3] not in other_moves:
                            return [2, 3]
                    
                    
                    #третий ряд
                    if (x_mouse >= 30 and y_mouse >= 350 and 
                        x_mouse <= 175 and y_mouse <= 460):
                        if [3, 1] not in my_moves and [3, 1] not in other_moves:
                            return [3, 1]
                    
                    if (x_mouse >= 185 and y_mouse >= 350 and 
                        x_mouse <= 330 and y_mouse <= 460):
                        if [3, 2] not in my_moves and [3, 2] not in other_moves:
                            return [3, 2]
                    
                    if (x_mouse >= 335 and y_mouse >= 350 and 
                        x_mouse <= 485 and y_mouse <= 460):
                        if [3, 3] not in my_moves and [3, 3] not in other_moves:
                            return [3, 3]
    
    #ход компа если он первый начинает ходить
    def firstComp(self, my_moves, other_moves):
        #первый ход
        if len(my_moves) == 0:
            return random.choice([[1,1], [1,3], [3,1], [3,3]]) 
        
        #второй ход
        if len(my_moves) == 1:
            if [2, 2] not in other_moves:
                if other_moves[0] not in [[1,1], [1,3], [3,1], [3,3]]:
                    return [2, 2]
                else:
                    if my_moves[0] in [[1,1], [3,3]] and other_moves[0] in [[1,1], [3,3]]:
                        return [2, 2]
                    if my_moves[0] in [[1,3], [3,1]] and other_moves[0] in  [[1,3], [3,1]]:
                        return [2, 2]
                    if my_moves[0][0] == other_moves[0][0]:
                        return [2, my_moves[0][1]]
                    if my_moves[0][1] == other_moves[0][1]:
                        return [my_moves[0][0], 2]
            else:
                if my_moves[0][0] == 1:
                    a = 3
                else: 
                    a = 1
                if my_moves[0][1] == 1:
                    b = 3
                else: 
                    b = 1
                return [a, b]
            
        #третий ход (остался только один вариант событий)
        #угол через пустую клетку
        if len(my_moves) == 2:
            if [my_moves[0][0], 2] not in other_moves:
                if my_moves[0][1] == 1:
                    if [my_moves[0][0], 3] not in my_moves and [my_moves[0][0], 3] not in other_moves:
                        return [my_moves[0][0], 3]
                else:
                    if [my_moves[0][0], 1] not in my_moves and [my_moves[0][0], 1] not in other_moves:
                        return [my_moves[0][0], 1]
            if [2, my_moves[0][1]] not in other_moves:
                if my_moves[0][0] == 1:
                    if [3, my_moves[0][1]] not in my_moves and [3, my_moves[0][1]] not in other_moves:
                        return [3, my_moves[0][1]]
                else:
                    if [1, my_moves[0][1]] not in my_moves and [1, my_moves[0][1]] not in other_moves:
                        return [1, my_moves[0][1]]
            
        #четвертый и пятый ход 
        #если игра зашла в тупик - выбираем любую пустую клетку
        empty = []
        a = 1
        while a <= self.n:
            b = 1
            while b <= self.n:
                if [a, b] not in my_moves and [a, b] not in other_moves:
                    empty.append([a, b])
                b += 1
            a += 1  
            
        return random.choice(empty) 
    
     
    #ход компа если он второй начинает ходить
    def secondComp(self, my_moves, other_moves):
        #первый ход
        if len(my_moves) == 0:
            if [2, 2] not in other_moves:
                return [2,2]
            return random.choice([[1,1], [1,3], [3,1], [3,3]])
        
        #второй ход
        if len(my_moves) == 1:
            if [2,2] in my_moves:
                arr = []
                for i in [[1,2], [2,1], [2,3], [3,2]]:
                   if i not in other_moves:
                       arr.append(i)
                return random.choice(arr)
            else:
                arr = []
                for i in [[1,1], [1,2], [1,3], [3,3]]:
                   if i not in other_moves:
                       arr.append(i)
                return random.choice(arr)
        
        #третий ход и дальше
        #если мы не блокируем тройку и не ставим ее сами, 
        #то не важен какой ход сделать
        empty = []
        a = 1
        while a <= self.n:
            b = 1
            while b <= self.n:
                if [a, b] not in my_moves and [a, b] not in other_moves:
                    empty.append([a, b])
                b += 1
            a += 1  
            
        return random.choice(empty) 
            
    #ход компа
    def compMove(self, my_moves, other_moves, pas):
        
        if pas == 1:
            return self.firstComp(my_moves, other_moves)
        if pas == 2:
            return self.secondComp(my_moves, other_moves)

#для поля 4*4
class Four:
    def __init__(self):
        self.n = 4
        self.img = pygame.image.load('pictures/field_4.png')
      
    #получение координат
    def getCoordinate(self, c):
        if c == [1, 1]:
            return (45, 45)
        if c == [1, 2]:
            return (155, 45)
        if c == [1, 3] :
            return (270, 45)
        if c == [1, 4] :
            return (380, 45)
        if c == [2, 1]:
            return (45, 140)
        if c == [2, 2]:
            return (155, 140)
        if c == [2, 3]:
            return (270, 140)
        if c == [2, 4] :
            return (380, 140)
        if c == [3, 1]:
            return (45, 228)
        if c == [3, 2]:
            return (155, 228)
        if c == [3, 3]:
            return (270, 228)
        if c == [3, 4] :
            return (380, 228)
        if c == [4, 1]:
            return (45, 315)
        if c == [4, 2]:
            return (155, 315)
        if c == [4, 3]:
            return (270, 315)
        if c == [4, 4] :
            return (380, 315)
    
    #для хода игрока на поле 4*4
    def humanMove(self, my_moves, other_moves):
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
                    
                    #первый ряд
                    if (x_mouse >= 35 and y_mouse >= 110 and 
                        x_mouse <= 140 and y_mouse <= 190):
                        if [1, 1] not in my_moves and [1, 1] not in other_moves:
                            return [1, 1]
                    
                    if (x_mouse >= 145 and y_mouse >= 110 and 
                        x_mouse <= 250 and y_mouse <= 190):
                        if [1, 2] not in my_moves and [1, 2] not in other_moves:
                            return [1, 2]
                    
                    if (x_mouse >= 260 and y_mouse >= 110 and 
                        x_mouse <= 360 and y_mouse <= 190):
                        if [1, 3] not in my_moves and [1, 3] not in other_moves:
                            return [1, 3]
                    
                    if (x_mouse >= 370 and y_mouse >= 110 and 
                        x_mouse <= 470 and y_mouse <= 190):
                        if [1, 4] not in my_moves and [1, 4] not in other_moves:
                            return [1, 4]
                        
                    #второй ряд
                    if (x_mouse >= 35 and y_mouse >= 195 and 
                        x_mouse <= 140 and y_mouse <= 275):
                        if [2, 1] not in my_moves and [2, 1] not in other_moves:
                            return [2, 1]
                    
                    if (x_mouse >= 145 and y_mouse >= 195 and 
                        x_mouse <= 250 and y_mouse <= 275):
                        if [2, 2] not in my_moves and [2, 2] not in other_moves:
                            return [2, 2]
                    
                    if (x_mouse >= 260 and y_mouse >= 195 and 
                        x_mouse <= 360 and y_mouse <= 275):
                        if [2, 3] not in my_moves and [2, 3] not in other_moves:
                            return [2, 3]
                    
                    if (x_mouse >= 370 and y_mouse >= 195 and 
                        x_mouse <= 470 and y_mouse <= 275):
                        if [2, 4] not in my_moves and [2, 4] not in other_moves:
                            return [2, 4]
                    
                    #третий ряд
                    if (x_mouse >= 35 and y_mouse >= 280 and 
                        x_mouse <= 140 and y_mouse <= 360):
                        if [3, 1] not in my_moves and [3, 1] not in other_moves:
                            return [3, 1]
                    
                    if (x_mouse >= 145 and y_mouse >= 280 and 
                        x_mouse <= 250 and y_mouse <= 360):
                        if [3, 2] not in my_moves and [3, 2] not in other_moves:
                            return [3, 2]
                    
                    if (x_mouse >= 260 and y_mouse >= 280 and 
                        x_mouse <= 360 and y_mouse <= 360):
                        if [3, 3] not in my_moves and [3, 3] not in other_moves:
                            return [3, 3]
                    
                    if (x_mouse >= 370 and y_mouse >= 280 and 
                        x_mouse <= 470 and y_mouse <= 360):
                        if [3, 4] not in my_moves and [3, 4] not in other_moves:
                            return [3, 4]
                        
                    #четвертый ряд
                    if (x_mouse >= 35 and y_mouse >= 375 and 
                        x_mouse <= 140 and y_mouse <= 455):
                        if [4, 1]not in my_moves and [4, 1] not in other_moves:
                            return [4, 1]
                    
                    if (x_mouse >= 145 and y_mouse >= 375 and 
                        x_mouse <= 250 and y_mouse <= 455):
                        if [4, 2] not in my_moves and [4, 2] not in other_moves:
                            return [4, 2]
                    
                    if (x_mouse >= 260 and y_mouse >= 375 and 
                        x_mouse <= 360 and y_mouse <= 455):
                        if [4, 3] not in my_moves and [4, 3] not in other_moves:
                            return [4, 3]
                    
                    if (x_mouse >= 370 and y_mouse >= 375 and 
                        x_mouse <= 470 and y_mouse <= 455):
                        if [4, 4] not in my_moves and [4, 4] not in other_moves:
                            return [4, 4]
    
    #ход компа
    #не придумал выиграшных ходов, поэтому написал то, 
    #что по моему мнению затруднит игру с компом
    #основа тактики - кучность ходов
    def compMove(self, my_moves, other_moves, pas):
        
        #первый ход
        if len(my_moves) == 0:
            a = random.choice([1, 2, 3, 4])
            b = random.choice([1, 2, 3, 4])
            if [a, b] not in other_moves:
                return [a, b]
            else:
                if b != self.n:
                    return [a, b+1]
                else:
                    return [a, b-1]
        
        #тактика кучности ходов
        if len(my_moves) + len(other_moves) <= self.n**2 - 2:
            
            arr = []
            for i in my_moves:
                a = [i[0] + 1, i[1]]
                if a[0] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
            
                a = [i[0] - 1, i[1]]
                if a[0] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
            
                a = [i[0], i[1] + 1]
                if a[1] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0], i[1] - 1]
                if a[1] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0] + 1, i[1] + 1]
                if a[0] <= self.n and a[1] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                        
                a = [i[0] - 1, i[1] - 1]
                if a[0] != 0 and a[1] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0] + 1, i[1] - 1]
                if a[0] <= self.n and a[1] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0] - 1, i[1] + 1]
                if a[0] != 0 and a[1] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
            
            if len(arr) != 0:
                return random.choice(arr)
            
        #ставим в оставшиеся пустые клетки
        empty = []
        a = 1
        while a <= self.n:
            b = 1
            while b <= self.n:
                if [a, b] not in my_moves and [a, b] not in other_moves:
                    empty.append([a, b])
                b += 1
            a += 1  
            
        return random.choice(empty) 

#для поля 5*5
class Five:
    def __init__(self):
        self.n = 5
        self.img = pygame.image.load('pictures/field_5.png')
        
    #получение координат
    def getCoordinate(self, c):
        if c == [1, 1]:
            return (30, 20)
        if c == [1, 2]:
            return (125, 20)
        if c == [1, 3] :
            return (217, 20)
        if c == [1, 4] :
            return (309, 20)
        if c == [1, 5]:
            return (408, 20)
        if c == [2, 1]:
            return (30, 100)
        if c == [2, 2]:
            return (125, 100)
        if c == [2, 3]:
            return (217, 100)
        if c == [2, 4] :
            return (309, 100)
        if c == [2, 5]:
            return (408, 100)
        if c == [3, 1]:
            return (30, 180)
        if c == [3, 2]:
            return (125, 180)
        if c == [3, 3]:
            return (217, 180)
        if c == [3, 4] :
            return (309, 180)
        if c == [3, 5]:
            return (408, 180)
        if c == [4, 1]:
            return (30, 260)
        if c == [4, 2]:
            return (125, 260)
        if c == [4, 3]:
            return (217, 260)
        if c == [4, 4] :
            return (309, 260)
        if c == [4, 5]:
            return (408, 260)
        if c == [5, 1]:
            return (30, 340)
        if c == [5, 2]:
            return (125, 340)
        if c == [5, 3]:
            return (217, 340)
        if c == [5, 4] :
            return (309, 340)
        if c == [5, 5]:
            return (408, 340)
    
    #для хода игрока на поле 5*5
    def humanMove(self, my_moves, other_moves):
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
                    
                    #первый ряд
                    if (x_mouse >= 25 and y_mouse >= 90 and 
                        x_mouse <= 115 and y_mouse <= 160):
                        if [1, 1] not in my_moves and [1, 1] not in other_moves:
                            return [1, 1]
                    
                    if (x_mouse >= 120 and y_mouse >= 90 and 
                        x_mouse <= 205 and y_mouse <= 160):
                        if [1, 2] not in my_moves and [1, 2] not in other_moves:
                            return [1, 2]
                    
                    if (x_mouse >= 210 and y_mouse >= 90 and 
                        x_mouse <= 295 and y_mouse <= 160):
                        if [1, 3] not in my_moves and [1, 3] not in other_moves:
                            return [1, 3]
                    
                    if (x_mouse >= 300 and y_mouse >= 90 and 
                        x_mouse <= 385 and y_mouse <= 160):
                        if [1, 4] not in my_moves and [1, 4] not in other_moves:
                            return [1, 4]
                    
                    if (x_mouse >= 390 and y_mouse >= 90 and 
                        x_mouse <= 475 and y_mouse <= 160):
                        if [1, 5] not in my_moves and [1, 5] not in other_moves:
                            return [1, 5]
                        
                    #второй ряд
                    if (x_mouse >= 25 and y_mouse >= 167 and 
                        x_mouse <= 115 and y_mouse <= 240):
                        if [2, 1] not in my_moves and [2, 1] not in other_moves:
                            return [2, 1]
                    
                    if (x_mouse >= 120 and y_mouse >= 167 and 
                        x_mouse <= 205 and y_mouse <= 240):
                        if [2, 2] not in my_moves and [2, 2] not in other_moves:
                            return [2, 2]
                    
                    if (x_mouse >= 210 and y_mouse >= 167 and 
                        x_mouse <= 295 and y_mouse <= 240):
                        if [2, 3] not in my_moves and [2, 3] not in other_moves:
                            return [2, 3]
                    
                    if (x_mouse >= 300 and y_mouse >= 167 and 
                        x_mouse <= 385 and y_mouse <= 240):
                        if [2, 4] not in my_moves and [2, 4] not in other_moves:
                            return [2, 4]
                    
                    if (x_mouse >= 390 and y_mouse >= 167 and 
                        x_mouse <= 475 and y_mouse <= 240):
                        if [2, 5] not in my_moves and [2, 5] not in other_moves:
                            return [2, 5]
                    
                    #третий ряд
                    if (x_mouse >= 25 and y_mouse >= 247 and 
                        x_mouse <= 115 and y_mouse <= 320):
                        if [3, 1] not in my_moves and [3, 1] not in other_moves:
                            return [3, 1]
                    
                    if (x_mouse >= 120 and y_mouse >= 247 and 
                        x_mouse <= 205 and y_mouse <= 320):
                        if [3, 2] not in my_moves and [3, 2] not in other_moves:
                            return [3, 2]
                    
                    if (x_mouse >= 210 and y_mouse >= 247 and 
                        x_mouse <= 295 and y_mouse <= 320):
                        if [3, 3] not in my_moves and [3, 3] not in other_moves:
                            return [3, 3]
                    
                    if (x_mouse >= 300 and y_mouse >= 247 and 
                        x_mouse <= 385 and y_mouse <= 320):
                        if [3, 4] not in my_moves and [3, 4] not in other_moves:
                            return [3, 4]
                    
                    if (x_mouse >= 390 and y_mouse >= 247 and 
                        x_mouse <= 475 and y_mouse <= 320):
                        if [3, 5] not in my_moves and [3, 5] not in other_moves:
                            return [3, 5]
                        
                    #четвертый ряд
                    if (x_mouse >= 25 and y_mouse >= 327 and 
                        x_mouse <= 115 and y_mouse <= 400):
                        if [4, 1] not in my_moves and [4, 1] not in other_moves:
                            return [4, 1]
                    
                    if (x_mouse >= 120 and y_mouse >= 327 and 
                        x_mouse <= 205 and y_mouse <= 400):
                        if [4, 2] not in my_moves and [4, 2] not in other_moves:
                            return [4, 2]
                    
                    if (x_mouse >= 210 and y_mouse >= 327 and 
                        x_mouse <= 295 and y_mouse <= 400):
                        if [4, 3] not in my_moves and [4, 3] not in other_moves:
                            return [4, 3]
                    
                    if (x_mouse >= 300 and y_mouse >= 327 and 
                        x_mouse <= 385 and y_mouse <= 400):
                        if [4, 4] not in my_moves and [4, 4] not in other_moves:
                            return [4, 4]
                    
                    if (x_mouse >= 390 and y_mouse >= 327 and 
                        x_mouse <= 475 and y_mouse <= 400):
                        if [4, 5] not in my_moves and [4, 5] not in other_moves:
                            return [4, 5]
                    
                    #пятыйй ряд
                    if (x_mouse >= 25 and y_mouse >= 407 and 
                        x_mouse <= 115 and y_mouse <= 480):
                        if [5, 1] not in my_moves and [5, 1] not in other_moves:
                            return [5, 1]
                    
                    if (x_mouse >= 120 and y_mouse >= 407 and 
                        x_mouse <= 205 and y_mouse <= 480):
                        if [5, 2] not in my_moves and [5, 2] not in other_moves:
                            return [5, 2]
                    
                    if (x_mouse >= 210 and y_mouse >= 407 and 
                        x_mouse <= 295 and y_mouse <= 480):
                        if [5, 3] not in my_moves and [5, 3] not in other_moves:
                            return [5, 3]
                    
                    if (x_mouse >= 300 and y_mouse >= 407 and 
                        x_mouse <= 385 and y_mouse <= 480):
                        if [5, 4] not in my_moves and [5, 4] not in other_moves:
                            return [5, 4]
                    
                    if (x_mouse >= 390 and y_mouse >= 407 and 
                        x_mouse <= 475 and y_mouse <= 480):
                        if [5, 5] not in my_moves and [5, 5] not in other_moves:
                            return [5, 5]
    
    #ход компа
    #тут так же (не придумал выиграшных ходов)
    #основа тактики - кучность ходов
    def compMove(self, my_moves, other_moves, pas):
        
        #первый ход
        if len(my_moves) == 0:
            if [3, 3] not in other_moves:
                return [3, 3]
            #ставим рядом с соперником
            return random.choice([[2,2], [2,3], [2,4], [3,2], [3,4], [4,2], [4,3], [4,4]])
        
        #тактика кучности ходов
        if len(my_moves) + len(other_moves) <= self.n**2 - 2:
            
            arr = []
            for i in my_moves:
                a = [i[0] + 1, i[1]]
                if a[0] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
            
                a = [i[0] - 1, i[1]]
                if a[0] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
            
                a = [i[0], i[1] + 1]
                if a[1] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0], i[1] - 1]
                if a[1] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0] + 1, i[1] + 1]
                if a[0] <= self.n and a[1] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                        
                a = [i[0] - 1, i[1] - 1]
                if a[0] != 0 and a[1] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0] + 1, i[1] - 1]
                if a[0] <= self.n and a[1] != 0:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
                    
                a = [i[0] - 1, i[1] + 1]
                if a[0] != 0 and a[1] <= self.n:
                    if a not in my_moves and a not in other_moves:
                        arr.append(a)
            
            if len(arr) != 0:
                return random.choice(arr)
         
        #ставим в оставшиеся пустые клетки
        empty = []
        a = 1
        while a <= self.n:
            b = 1
            while b <= self.n:
                if [a, b] not in my_moves and [a, b] not in other_moves:
                    empty.append([a, b])
                b += 1
            a += 1  
            
        return random.choice(empty)

        
#класс для работы с полями и ходами  (перенаправлятор)
class Field:
    
    def __init__(self, n, player1, player2):
        self.n = n
        self.moves_player1 = []
        self.moves_player2 = []
        self.who_player1 = player1
        self.who_player2 = player2
        
        self.field_face = pygame.Surface((500, 500))
        
        if n == 3:
            self.size = Three()
        if n == 4:
            self.size = Four()
        if n == 5:
            self.size = Five()
        
        
        self.field_face.blit(self.size.img, (0,0))
     
    #проверка победы
    def win(self, player):
        
        n = self.n
        if player == 1:
            copy = self.moves_player1
        else:
            copy = self.moves_player2
        
        #проверка горизонталей и вертикалей
        for i in range(0, len(copy)-2):
            count = 1
            for el in copy[i+1:]:
                if copy[i][0] == el[0]:
                    count += 1
                if count == n:
                    return 1
                
            count = 1
            for el in copy[i+1:]:
                if copy[i][1] == el[1]:
                    count += 1
                if count == n:
                    return 1
        
        #проверка диагоналей
        w = 1
        a = 1
        while a <= n:
            if [a, a] not in copy:
                w = 0
                break
            a += 1
            
        if w == 1:
            return 1
        else:
            a = 1
            while a <= n:
                if [a, n-a+1] not in copy:
                    return 0
                a += 1
            return 1
        
        return 0
    
    #пустая клетка
    def inEmpty(self):
        a = 1
        while a <= self.n:
            b = 1
            while b <= self.n:
                if [a, b] not in self.moves_player1 and [a, b] not in self.moves_player2:
                    return [a, b]
                b += 1
            a += 1  
            
        return []
    
    #проверка возможной победы
    def possibleWin(self, moves, finish_move):
        
        n = self.n
        copy = moves
       #copy.append(finish_move)
        
        #проверка горизонталей и вертикалей
        count = 1
        for el in copy:
            if finish_move[0] == el[0]:
                count += 1
            if count == n:
                return 1
           
        count = 1
        for el in copy:
            if finish_move[1] == el[1]:
                count += 1
            if count == n:
                return 1
        
        #проверка диагоналей
        w = 1
        a = 1
        while a <= n:
            if [a, a] not in copy:
                if finish_move != [a, a]:
                    w = 0
                    break
            a += 1
            
        if w == 1:
            return 1
        else:
            a = 1
            while a <= n:
                if [a, n-a+1] not in copy:
                    if finish_move != [a, n-a+1]:
                        return 0
                a += 1
            return 1
        
        return 0
    
    #возможна ли победа (линия)
    def ifWin(self, moves):
        if len(moves) > 1:
            
            a = 1
            while a <= self.n:
                b = 1
                while b <= self.n:
                    if [a, b] not in self.moves_player1 and [a, b] not in self.moves_player2:
                        if self.possibleWin(moves, [a, b]):
                            return [a, b]
                    b += 1
                a += 1  
                    
            return []
        return []
    
    #вызов нужной функции хода
    def move(self, player, pas, number_move):
        
        #pas - для принятия тактики компьютера, мешать или выигровать
        
        if player == 1:
            if self.who_player1 == 1:
                move = self.size.humanMove(self.moves_player1, self.moves_player2)
                self.moves_player1.append(move)
                return self.size.getCoordinate(move)
            
            if self.who_player1 == 2:
                
                time.sleep(1)
                if number_move >= 2*self.n - 3:
                    #если могу победить - побеждаю
                    position = self.ifWin(self.moves_player1)
                    if len(position) != 0:
                        move = position
                        self.moves_player1.append(move)
                        return self.size.getCoordinate(move)
                    
                    #если может победить противник - препятствую
                    position = self.ifWin(self.moves_player2)
                    if len(position) != 0:
                        move = position
                        self.moves_player1.append(move)
                        return self.size.getCoordinate(move)
                
                move = self.size.compMove(self.moves_player1, self.moves_player2, pas)
                self.moves_player1.append(move)
                return self.size.getCoordinate(move)
        
        if player == 2:
            if self.who_player2 == 1:
                move = self.size.humanMove(self.moves_player1, self.moves_player2)
                self.moves_player2.append(move)
                return self.size.getCoordinate(move)
            
            if self.who_player2 == 2:
                
                time.sleep(1)
                if number_move >= 2*self.n - 3:
                    #если могу победить - побеждаю
                    position = self.ifWin(self.moves_player2)
                    if len(position) != 0:
                        move = position
                        self.moves_player2.append(move)
                        return self.size.getCoordinate(move)
                    
                    #если может победить противник - препятствую
                    position = self.ifWin(self.moves_player1)
                    if len(position) != 0:
                        move = position
                        self.moves_player2.append(move)
                        return self.size.getCoordinate(move)
                
                move = self.size.compMove(self.moves_player2, self.moves_player1, pas)
                self.moves_player2.append(move)
                return self.size.getCoordinate(move)
      
    
    #отчистка массивов ходов
    def to_empty(self):
        self.moves_player1 = []
        self.moves_player2 = []
