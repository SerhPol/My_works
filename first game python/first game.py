import pygame
#pygame - библиотека для игры

print('Welcome to the game !!! \nWould you like to read the rules? \n  1 - Yes \n  2 - No')
if input() == '1':
    f = open('rules.txt')
    print(f.read())
    f.close()
    
#ввод и создание персонажей
#игрок 1
print("\nWrite down the first player's name:")
name1 = str(input())
print("Choose a warrior:\n  1 - Fighter \n  2 - Archer")
choice1 = int(input())

#игрок 2
print("Write down the second player's name:")
name2 = str(input())
print("Choose a warrior:\n  1 - Fighter \n  2 - Archer")
choice2 = int(input())

#начало действия игры
pygame.init()


##########

#класс игрока
class Person:
    def __init__(self, name):
        self.name = name

#персонаж
class Warrior(Person):
    face = pygame.Surface((40, 40))
    def __init__(self, name, x = 0, y = 0, health = 100, damage = 10):
        Person.__init__(self, name)
        self.health = health
        self.damage = damage
        self.x = x
        self.y = y

    #предотвращение захода игрока на игрока, sx и sy измененые координаты 
    def inter_person_to_person(self, sx, sy, x, y):
        if sx == x:
            if sy == y:
                return 0
        return 1


    
#персонаж - лучник
class Archer(Warrior):
    
    def __init__(self, name, x, y, health = 100, damage = 10):
        Warrior.__init__(self, name, x, y, health, damage)
        self.arrow = self.Arrow()
        self.strike = False  #возможность удара(выстрела)
        #рисунки
        self.img_arch = pygame.image.load('archer.png')   #pygame.image - Загружает и сохраняет изображение
        
    #функция выстрела
    def attack(self, route_buf):
        self.strike = True
        self.arrow.route = route_buf
        self.arrow.x = self.x
        self.arrow.y = self.y

    #обработка попадания
    def inter(self, other_player):
        if self.arrow.inter(other_player.x, other_player.y) == 1:
            other_player.health -= self.damage
            self.strike = False
            self.arrow.x = 1000
            self.arrow.y = 1000

    #вставка картинки на месте лучника и стрел
    def image(self):
        self.face.blit(self.img_arch, (0,0))
        screen.blit(self.face, (self.x, self.y))
        self.arrow.image()

    #полет стрелы
    def attack_fly(self):
        if self.strike == True:
            if self.arrow.flight() == 0:
                self.strike = False

    #стрела
    class Arrow:  
        face_vert = pygame.Surface((20, 40)) #pygame.Surface — объект для представления изображений
        face_hor = pygame.Surface((40, 20))
        def __init__(self, x = 1000, y = 1000):
            self.x = x
            self.y = y
            self.route = 'up'
            #рисунки
            self.img_arr_up = pygame.image.load('arrow_up.png')
            self.img_arr_down = pygame.image.load('arrow_down.png')
            self.img_arr_left = pygame.image.load('arrow_left.png')
            self.img_arr_right = pygame.image.load('arrow_right.png')

        #полет стрелы
        def flight(self):
            if self.route == 'up':
                self.y -= 2
                if self.y < 0:
                    self.x = 1000
                    self.y = 1000
                    return 0
            if self.route == 'down':
                self.y += 2
                if self.y > 440:
                    self.x = 1000
                    self.y = 1000
                    return 0
            if self.route == 'left':
                self.x -= 2
                if self.x < 0:
                    self.x = 1000
                    self.y = 1000
                    return 0
            if self.route == 'right':
                self.x += 2
                if self.x > 520:
                    self.x = 1000
                    self.y = 1000
                    return 0
            return 1
            

        #функция расчета попадания
        #x2, y2 - other player
        def inter(self, x2, y2):
            if self.route == 'up':
                if self.x >= x2 and self.x +20 <= x2+40 and self.y <= y2+20 and self.y >= y2:
                    return 1
                else:
                    return 0
            if self.route == 'down':
                if self.x >= x2 and self.x +20 <= x2+40 and self.y+40 >= y2+20 and self.y <= y2+40:
                    return 1
                else:
                    return 0
            if self.route == 'left':
                if self.y >= y2 and self.y +20 <= y2+40 and self.x <= x2+20 and self.x >= x2:
                    return 1
                else:
                    return 0
            if self.route == 'right':
                if self.y >= y2 and self.y +20 <= y2+40 and self.x <= x2+20 and self.x >= x2:
                    return 1
                else:
                    return 0

        #загрузка картинок стрелы
        def image(self):
            if self.route == 'up':
                self.face_vert.blit(self.img_arr_up, (0,0))
                screen.blit(self.face_vert, (self.x, self.y))
            if self.route == 'down':
                self.face_vert.blit(self.img_arr_down, (0,0))
                screen.blit(self.face_vert, (self.x, self.y))
            if self.route == 'left':
                self.face_hor.blit(self.img_arr_left, (0,0))
                screen.blit(self.face_hor, (self.x, self.y))
            if self.route == 'right':
                self.face_hor.blit(self.img_arr_right, (0,0))
                screen.blit(self.face_hor, (self.x, self.y))


######

#персонаж - воин
class Fighter(Warrior):

    def __init__(self, name, x, y, health = 150, damage = 15):
        Warrior.__init__(self, name, x, y, health, damage)
        self.sword = self.Sword()
        self.strike = False  #возможность удара
        self.img_fight = pygame.image.load('fighter.png')

    #функция атаки
    def attack(self, route_buf):
        self.strike = True
        self.sword.route = route_buf
        self.sword.x = self.x
        self.sword.y = self.y
        #координаты сохранения места откуда был произведен удар
        self.sword.xs = self.x 
        self.sword.ys = self.y

    #обработка попадания
    def inter(self, other_player):
        if self.sword.inter(other_player.x, other_player.y) == 1:
            other_player.health -= self.damage
            self.strike = False
            self.sword.x = 1000
            self.sword.y = 1000

    #вставка картинки на месте воина и меча
    def image(self):
        self.face.blit(self.img_fight, (0,0))
        screen.blit(self.face, (self.x, self.y))
        self.sword.image()

    #полет меча
    def attack_fly(self):
        if self.strike == True:
            if self.sword.flight() == 0:
                self.strike = False
                    

    #меч
    class Sword:  
        face_vert = pygame.Surface((20, 40)) #pygame.Surface — объект для представления изображений
        face_hor = pygame.Surface((40, 20))
        def __init__(self, x = 1000, y = 1000):
            self.x = x
            self.y = y
            self.xs = x
            self.ys = y
            self.route = 'up'
            self.img_sword_up = pygame.image.load('sword_up.png')
            self.img_sword_down = pygame.image.load('sword_down.png')
            self.img_sword_left = pygame.image.load('sword_left.png')
            self.img_sword_right = pygame.image.load('sword_right.png')

        #полет меча
        def flight(self):
            if self.route == 'up':
                self.y -= 2
                if self.y < self.ys-60:
                    self.x = 1000
                    self.y = 1000
                    return 0
            if self.route == 'down':
                self.y += 2
                if self.y > self.ys+60:
                    self.x = 1000
                    self.y = 1000
                    return 0
            if self.route == 'left':
                self.x -= 2
                if self.x < self.xs-60:
                    self.x = 1000
                    self.y = 1000
                    return 0
            if self.route == 'right':
                self.x += 2
                if self.x > self.xs+70:
                    self.x = 1000
                    self.y = 1000
                    return 0
            return 1
            

        #функция расчета попадания
        #x2, y2 - other player
        def inter(self, x2, y2):
            if self.route == 'up':
                if self.x >= x2 and self.x +20 <= x2+40 and self.y <= y2+20 and self.y >= y2:
                    return 1
                else:
                    return 0
            if self.route == 'down':
                if self.x >= x2 and self.x +20 <= x2+40 and self.y+40 >= y2+20 and self.y <= y2+40:
                    return 1
                else:
                    return 0
            if self.route == 'left':
                if self.y >= y2 and self.y +20 <= y2+40 and self.x <= x2+20 and self.x >= x2:
                    return 1
                else:
                    return 0
            if self.route == 'right':
                if self.y >= y2 and self.y +20 <= y2+40 and self.x+40<= x2+20 and self.x+40 >= x2:
                    return 1
                else:
                    return 0

        #загрузка картинок меча
        def image(self):
            if self.route == 'up':
                self.face_vert.blit(self.img_sword_up, (0,0))
                screen.blit(self.face_vert, (self.x, self.y))
            if self.route == 'down':
                self.face_vert.blit(self.img_sword_down, (0,0))
                screen.blit(self.face_vert, (self.x, self.y))
            if self.route == 'left':
                self.face_hor.blit(self.img_sword_left, (0,0))
                screen.blit(self.face_hor, (self.x, self.y))
            if self.route == 'right':
                self.face_hor.blit(self.img_sword_right, (0,0))
                screen.blit(self.face_hor, (self.x, self.y))


########
#продлжать игру или нет
answer = '1'

while answer == '1':

    #создание окна для игры
    window = pygame.display.set_mode((520, 510))  #pygame.display-Доступ к дисплею

    #создание поля для игры
    screen = pygame.Surface((520, 440))  #pygame.Surface - Управляет изображениями и экраном

    #игрок 1 и игрок 2
    if choice1 == 1:
        person1 = Fighter(name1, 80, 80)
    else:
        person1 = Archer(name1, 80, 80)

    if choice2 == 1:
        person2 = Fighter(name2,320, 360)
    else:
        person2 = Archer(name2, 320, 360)

    #для теста
    #person1 = Archer("Den", 80, 80)
    #person2 = Archer("Dark", 320, 360)
    #person2 = Fighter("Dark", 320, 360)

    #для сохранения направления стрельбы
    route_buf1 = 'down'
    route_buf2 = 'up'


    #для надписи
    myfont = pygame.font.SysFont('monoscpace', 25)  #pygame.font - Использует системные шрифты

    #для завершения цикла
    done = False

    #цикл абработки действий
    while done == False:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:  #нажатие на крестик
                done = True
                answer = '2'
            #pygame.KEYDOWN - Считывает нажатия клавиш с клавиатуры
            #передвижение
            if e.type == pygame.KEYDOWN and e.key == pygame.K_s and person1.y+40 <= 420:
                route_buf1 = 'down'
                if person1.inter_person_to_person(person1.x, person1.y+40, person2.x, person2.y):
                    person1.y += 40
            if e.type == pygame.KEYDOWN and e.key == pygame.K_w and person1.y-40 >= 0:
                route_buf1 = 'up'
                if person1.inter_person_to_person(person1.x, person1.y-40, person2.x, person2.y):
                    person1.y -= 40
            if e.type == pygame.KEYDOWN and e.key == pygame.K_a and person1.x-40 >= 0:
                route_buf1 = 'left'
                if person1.inter_person_to_person(person1.x-40, person1.y, person2.x, person2.y):
                    person1.x -= 40
            if e.type == pygame.KEYDOWN and e.key == pygame.K_d and person1.x+40 <= 500:
                route_buf1 = 'right'
                if person1.inter_person_to_person(person1.x+40, person1.y, person2.x, person2.y):
                    person1.x += 40

            #передвижение второго
            if e.type == pygame.KEYDOWN and e.key == pygame.K_DOWN  and person2.y+40 <= 420:
                route_buf2 = 'down'
                if person1.inter_person_to_person(person2.x, person2.y+40, person1.x, person1.y):
                    person2.y += 40
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP and person2.y-40 >= 0:
                route_buf2 = 'up'
                if person1.inter_person_to_person(person2.x, person2.y-40, person1.x, person1.y):
                    person2.y -= 40
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT and person2.x-40 >= 0:
                route_buf2 = 'left'
                if person1.inter_person_to_person(person2.x-40, person2.y, person1.x, person1.y):
                    person2.x -= 40
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT and person2.x+40 <= 500:
                route_buf2 = 'right'
                if person1.inter_person_to_person(person2.x+40, person2.y, person1.x, person1.y):
                    person2.x += 40

        
            #выстрел 1
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                if person1.strike == False:
                    person1.attack(route_buf1)
                    

            #выстрел второго
            if e.type == pygame.KEYDOWN and e.key == pygame.K_KP_ENTER:
                if person2.strike == False:
                    person2.attack(route_buf2)

    #полет стрелы 1
        person1.attack_fly()
    
    #полет стрелы 2
        person2.attack_fly()
        
    #попадание первым во второго 
        person1.inter(person2)
        
    #попадание вторым в первого  
        person2.inter(person1)


        #строка жизней
        string = myfont.render('Health ' + person1.name + ' : ' + str(person1.health), 0, (200, 0, 0))
        string2 = myfont.render('Health ' + person2.name + ' : ' + str(person2.health), 0, (200, 0, 0))
  
        screen.fill((0, 0, 0))       #зарисовка поля чёрным (RGB)

        #размещение картинки на игроках и ударах(стрелы, мечы) 
        person1.image()
        person2.image()
    
        window.fill((200, 200, 200)) #зарисовка окна серым
        window.blit(screen, (0, 70)) #размешения поля на экране

        window.blit(string, (10, 10)) #размещение надписи
        window.blit(string2, (200, 10)) #размещение надписи


        #конец боя и вопрос о продолжении игры
        if answer == '1':
            if person1.health <= 0:
                done = True
                pygame.display.update()
                print('\nThe winner is player number two, ' + person2.name)
                print('Do you want to play more?\n 1 - Yes\n 2 - No')
                answer = str(input())
            if person2.health <= 0:
                done = True
                pygame.display.update()
                print('\nThe winner is player number one, ' + person1.name)
                print('Do you want to play more?\n 1 - Yes\n 2 - No')
                answer = str(input())

        pygame.display.update()



#конец игры
pygame.quit()


