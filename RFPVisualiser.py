from graphics import *
from operator import itemgetter
from random import randint


AXIS_X = 700
AXIS_Y = 700
SCALE = 8

def main():
    win = GraphWin("Visualiser", AXIS_X, AXIS_Y)
    win.setBackground(color_rgb(0, 0, 0))

    # Display Room
    room = [(0, 0), (10, 0), (10, 10), (0, 10)]

    largestx, largesty = 0, 0   # Track current coord placement positions

    for coord in room:
        largestx = coord[0] if coord[0] > largestx else largestx
        largesty = coord[1] if coord[1] > largesty else largesty

    displayPoints = []

    for coord in room:
        print(coord[0], coord[1])
        displayPoints.append(Point(coord[0] * SCALE, coord[1] * SCALE))

    display = Polygon(displayPoints)
    display.setFill(color_rgb(66, 134, 244))
    display.draw(win)

    print("Largestx: ", largestx, " Largesty: ", largesty)

    # Display Furniture
    example = [[(0, 0), (3, 0), (3, 3), (0, 3)]]
    example2 = [[(0, 0), (3, 0), (3, 3), (0, 3)], [(0, 0), (5, 0), (5, 5), (0, 5)], [(0, 0), (8, 0), (8, 8), (0, 8)], [(0, 0), (3, 0), (3, 3), (0, 3)], [(0, 0), (3, 0), (3, 3), (0, 3)],
                [(0, 0), (-4.378116341818308, 1.0402390578628915), (-5.4183553996812, -3.3378772839554167), (-1.0402390578628937, -4.378116341818307)]]

    for index, furniture in enumerate(example2):
        points = []

        largestx = max(furniture, key=itemgetter(1))[0]
        largesty = max(furniture, key=itemgetter(1))[1]
        print("Largestx: ", largestx, " Largesty: ", largesty)

        posx = randint(1, AXIS_X/10)
        posy = randint(1, AXIS_Y/10)

        for coord in furniture:
            points.append(Point((coord[0] + posx) * SCALE, (coord[1] + posy) * SCALE))

        display = Polygon(points)
        display.setFill(color_rgb(255, 255, 255))
        display.draw(win)

    win.getMouse()
    win.close()

main()