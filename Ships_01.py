from random import randint
class Player:
    def __init__(self,name,human):
        self.name = name
        self.human = human

class Ship:
    def __init__(self,lenght,horiz_orien):
        self.hor_coord = randint(0, 5)
        self.ver_coord = randint(0, 5)
        self.lenght = lenght
        self.horiz_orien = horiz_orien

        def cross(j,v,h):
            if coords[j][0] == v - 1 or \
                coords[j][0] == v + 1 or \
                coords[j][1] == h - 1 :
                #coords[j][1] == h + 1 :
                return "true"
            else:
                return "false"


        if len(coords)>1:

            for j in range(len(coords)):
                while self.ver_coord == coords[j][0] and self.hor_coord == coords[j][1] or \
                        cross(j,self.ver_coord,self.hor_coord) == "true":
                        self.hor_coord = randint(0, 5)
                        self.ver_coord = randint(0, 5)

            if self.lenght > 1:
                if horiz_orien == True:
                    if self.lenght == 2: #длина корабля = 2
                        for j in range(len(coords)):
                            while self.ver_coord == coords[j][0] and self.hor_coord == coords[j][1] or \
                                    self.ver_coord == coords[j][0] and self.hor_coord + 1 == coords[j][1] or \
                                    (self.hor_coord + self.lenght - 1) > 5 or \
                                    cross(j, self.ver_coord, self.hor_coord) == "true" or \
                                    cross(j,self.ver_coord,self.hor_coord + 1) == "true":
                                self.hor_coord = randint(0, 5)
                                self.ver_coord = randint(0, 5)
                        coords.append([self.ver_coord, self.hor_coord])
                        coords.append([self.ver_coord, self.hor_coord + 1])
                    if self.lenght == 3: #длина корабля = 3
                        for j in range(len(coords)):
                            while self.ver_coord == coords[j][0] and self.hor_coord == coords[j][1] or \
                                    self.ver_coord == coords[j][0] and self.hor_coord + 1 == coords[j][1] or \
                                    self.ver_coord == coords[j][0] and self.hor_coord + 2 == coords[j][1] or \
                                    (self.hor_coord + self.lenght - 1) > 5 or \
                                    cross(j, self.ver_coord, self.hor_coord) == "true" or \
                                    cross(j,self.ver_coord,self.hor_coord + 1) == "true" or \
                                    cross(j,self.ver_coord,self.hor_coord + 2) == "true":
                                self.hor_coord = randint(0, 5)
                                self.ver_coord = randint(0, 5)
                        coords.append([self.ver_coord, self.hor_coord])
                        coords.append([self.ver_coord, self.hor_coord + 1])
                        coords.append([self.ver_coord, self.hor_coord + 2])
                else:
                    if self.lenght == 2:
                        for j in range(len(coords)):
                            while self.ver_coord == coords[j][0] and self.hor_coord == coords[j][1] or \
                            self.ver_coord + 1 == coords[j][0] and self.hor_coord == coords[j][1] or \
                            (self.ver_coord + self.lenght - 1) > 5 or \
                            cross(j, self.ver_coord, self.hor_coord) == "true" or \
                            cross(j, self.ver_coord + 1, self.hor_coord) == "true":
                                self.hor_coord = randint(0, 5)
                                self.ver_coord = randint(0, 5)
                        coords.append([self.ver_coord, self.hor_coord])
                        coords.append([self.ver_coord + 1, self.hor_coord])
                    if self.lenght == 3:
                        for j in range(len(coords)):
                            while self.ver_coord == coords[j][0] and self.hor_coord == coords[j][1] or \
                                self.ver_coord + 1 == coords[j][0] and self.hor_coord == coords[j][1] or \
                                self.ver_coord + 2 == coords[j][0] and self.hor_coord == coords[j][1] or \
                                (self.ver_coord + self.lenght - 1) > 5 or \
                                cross(j, self.ver_coord, self.hor_coord) == "true" or \
                                cross(j, self.ver_coord + 1, self.hor_coord) == "true" or \
                                cross(j, self.ver_coord + 2, self.hor_coord) == "true":
                                self.hor_coord = randint(0, 5)
                                self.ver_coord = randint(0, 5)
                        coords.append([self.ver_coord, self.hor_coord])
                        coords.append([self.ver_coord + 1, self.hor_coord])
                        coords.append([self.ver_coord + 2, self.hor_coord])
            else:
                coords.append([self.ver_coord, self.hor_coord])
        else:
            coords.append([self.ver_coord, self.hor_coord])


class Board:
    def __init__(self,size,visible):
        self.size = size    #размер поля
        self.visible = visible  #видимость кораблей для противника
        self.field = [['0']*size for i in range(6)]    #массив поля
        self.ships = []     #массив где лежат все корабли
        self.busy_dots = []  #массив занятых точек
        self.victims = 0 #пораженные корабли
    def __str__(self):
        real_field = '--1-2-3-4-5-6'
        for i, row in enumerate(self.field):
            real_field += f'\n{i + 1}-' + '-'.join(row) + '-'
        return real_field

    def add_ship_auto(self):
        for i in range(len(coords)):
            self.field[coords[i][0]][coords[i][1]] = '■'
            self.busy_dots = coords

player1=Player('Вася',True)
player2=Player('LG',False)
coords=[]
score=0
board1 = Board(6,False)
board2 = Board(6,True)
ship1 = Ship(1,True)
ship2 = Ship(1,True)
ship3 = Ship(1,True)
ship4 = Ship(1,True)
ship5 = Ship(2,False)
ship6 = Ship(2,False)
ship7 = Ship(3,True)
board1.add_ship_auto()
board2.add_ship_auto()
# board2.add_ship_auto(ship2)
# board2.add_ship_auto(ship3)
# board2.add_ship_auto(ship4)
# board2.add_ship_auto(ship5)
# board2.add_ship_auto(ship6)
# board2.add_ship_auto(ship7)
print('busy dots 1st player: ',board1.busy_dots)
print('busy dots 2nd player: ',board2.busy_dots)
print('coords: ',coords)
print('lenght of coords: ',len(coords))
print('поле игрока ' + str(player1.name)+'\n'+str(board1))
print('поле игрока ' + str(player2.name)+'\n'+str(board2))