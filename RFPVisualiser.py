from graphics import *
from operator import itemgetter
from random import randint


AXIS_X = 1000
AXIS_Y = 700
SCALE = 10

def main():
    win = GraphWin("Visualiser", AXIS_X, AXIS_Y)
    win.setBackground(color_rgb(0, 0, 0))

    # Display Furniture
    example = [[(0, 0), (3, 0), (3, 3), (0, 3)]]
    example2 = [[(0, 0), (3, 0), (3, 3), (0, 3)], [(0, 0), (5, 0), (5, 5), (0, 5)], [(0, 0), (8, 0), (8, 8), (0, 8)], [(0, 0), (3, 0), (3, 3), (0, 3)], [(0, 0), (3, 0), (3, 3), (0, 3)],
                [(0, 0), (-4.378116341818308, 1.0402390578628915), (-5.4183553996812, -3.3378772839554167), (-1.0402390578628937, -4.378116341818307)]]

    data = [[(0, 0), (4, 0), (4, 10), (0, 10), (40, 40.0)], [(0, 0), (4, 0), (4, 10), (0, 10), (40, 40.0)], [(0, 0), (6, 0), (0, 10), (30, 30.0)], [(0, 0), (6, 0), (0, 10), (30, 30.0)], [(0, 0), (3, 0), (3, 5), (-3, 5), (23, 22.5)], [(0, 0), (3, 0), (3, 5), (-3, 5), (23, 22.5)], [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767), (21, 21.25502559083609)], [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767), (21, 21.25502559083609)], [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767), (21, 21.25502559083609)], [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767), (21, 21.25502559083609)], [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767), (21, 21.25502559083609)], [(0, 0), (4.610317298281767, 0), (4.6103172982817675, 4.610317298281767), (0, 4.610317298281767), (21, 21.25502559083609)], [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)], [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)], [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)], [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)], [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)], [(0, 0), (3.5, 0), (3.5000000000000004, 3.4999999999999996), (0, 3.5), (12, 12.25)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (3, 0), (3, 3), (0, 3), (9, 9.0)], [(0, 0), (0, 5), (-3, 5), (8, 7.5)], [(0, 0), (0, 5), (-3, 5), (8, 7.5)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.4788689868556624, 0), (2.4788689868556624, 2.4788689868556624), (0, 2.4788689868556624), (6, 6.144791453994818)], [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833), (5, 5.313756397709023)], [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833), (5, 5.313756397709023)], [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833), (5, 5.313756397709023)], [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833), (5, 5.313756397709023)], [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833), (5, 5.313756397709023)], [(0, 0), (2.3051586491408833, 0), (2.3051586491408838, 2.3051586491408833), (0, 2.3051586491408833), (5, 5.313756397709023)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (2, 0), (2, 2), (0, 2), (4, 4.0)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)], [(0, 0), (1.5, 0), (1.5, 1.4999999999999998), (0, 1.5), (2, 2.25)]]

    for index, furniture in enumerate(data):
        furniturePoints = []

        largestx = max(furniture, key=itemgetter(1))[0]
        largesty = max(furniture, key=itemgetter(1))[1]

        posx = randint(1, round(AXIS_X))
        posy = randint(1, round(AXIS_Y))

        for coord in furniture[:-1]:
            furniturePoints.append(Point((coord[0] - largestx) * SCALE + posx, (coord[1] - largesty) * SCALE + posy))

        display = Polygon(furniturePoints)
        display.setFill(color_rgb(255, 255, 255))
        display.draw(win)

    # Display Room
    room = [(0, 0), (10, 0), (10, 10), (0, 10)]

    largestx = max(room, key=itemgetter(1))[0]
    largesty = max(room, key=itemgetter(1))[1]

    roomPoints = []

    for coord in room:
        roomPoints.append(Point(((coord[0] - largestx/2) * SCALE) + AXIS_X/2, ((coord[1] - largesty/2) * SCALE) + AXIS_Y/2))

    display = Polygon(roomPoints)
    display.setFill(color_rgb(66, 134, 244))
    display.draw(win)

    win.getMouse()
    win.close()

main()