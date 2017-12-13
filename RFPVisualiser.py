from graphics import *
from operator import itemgetter
from random import randint
import ast

AXIS_X = 1000
AXIS_Y = 700
SCALE = 100

def parse(program, question):
    arr_tuples = []
    with open(program) as f:
        line = f.readline()

        for i, line in enumerate(f):
            if i == question - 2:
                beg = line.split("#")[0]
                problem_num = beg.split(":")[0]
                room = ast.literal_eval("[{}]".format(beg.split(":")[1]))
                all_shapes = line.split("#")[1].split(";")

                print("Problem", problem_num)
                print("Room vertices", room)

                # furniture shapes stored as a list of a list of tuples
                # meaning each furniture is a list of tuples, so the whole list of furniture
                # is a list of list of tuples
                for i in range(0, len(all_shapes)):
                    shape = all_shapes[i].split(":")
                    cost = shape[0].split()[0] # think about how cost will be stored in the list
                    vertices = shape[1]
                    vertices_tuple = ast.literal_eval("[{}]".format(vertices))
                    arr_tuples += [vertices_tuple]
                    # store the cost and area in the last tuple
                    arr_tuples[i].append((ast.literal_eval(cost), find_area(vertices_tuple)))
                    #print(i, "Cost is", cost, "for this shape", vertices)

# sorting furniture list based on max area
    arr_tuples = sorted(arr_tuples, key=lambda x: x[-1][1], reverse=True)
    return room, arr_tuples

def find_area(vertices):
    area = 0.0
    for i in range(len(vertices)):
        if (i + 1 < len(vertices)):
            # all values casted to float
            area += ((float)(vertices[i][0])*(float)(vertices[i+1][1])) - ((float)(vertices[i][1])*(float)(vertices[i+1][0]))
    area += ((float)(vertices[-1][0])*(float)(vertices[0][1])) - ((float)(vertices[-1][0])*(float)(vertices[0][1]))
    area = area / 2
    return area


def main(room, furniture):
    win = GraphWin("Visualiser", AXIS_X, AXIS_Y)
    win.setBackground(color_rgb(0, 0, 0))

    # Display Furniture
    for index, furniture in enumerate(furniture):
        furniturePoints = []

        largestx = max(furniture, key=itemgetter(1))[0]
        largesty = max(furniture, key=itemgetter(1))[1]

        posx = randint(1, round(AXIS_X))
        posy = randint(1, round(AXIS_Y))

        for coord in furniture[:-1]:
            furniturePoints.append(Point((coord[0] - largestx) * SCALE + posx, (coord[1] - largesty) * SCALE + posy))

        weight = round(furniture[-1][1])

        display = Polygon(furniturePoints)
        display.setFill(color_rgb(255, 20, 100))
        display.draw(win)

    # Display Room
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


def onTop(room, furniture):
    win = GraphWin("Visualiser", AXIS_X, AXIS_Y)
    win.setBackground(color_rgb(0, 0, 0))

    # Room
    roomPoints = []

    for coord in room:
        roomPoints.append(Point(coord[0] * SCALE + 100, coord[1] * SCALE + 100))

    display = Polygon(roomPoints)
    display.setFill(color_rgb(66, 134, 244))
    display.draw(win)

    # Furniture
    for index, furniture in enumerate(furniture):
        furniturePoints = []

        for coord in furniture[:-1]:
            furniturePoints.append(Point(coord[0] * SCALE + 100, coord[1] * SCALE + 100))

        weight = round(furniture[-1][1]*3)

        display = Polygon(furniturePoints)
        display.setFill(color_rgb(255, 20, 100))
        display.draw(win)

    win.getMouse()
    win.close()

q5sol = [[(0.36512, 1.17319), (-0.40234170553594284, 0.7681925594915511), (0.002655734972506485, 0.0007308539556081239), (0.7701174405084484, 0.405728294464057), (0.36512, 1.17319)], [(0.81809, 1.69963), (0.40342535545446334, 1.8273340783787144), (0.2757212770757488, 1.4126694338331778), (0.6903859216212856, 1.284965355454463), (0.81809, 1.69963)]]

room, furniture = parse("input.txt", 5)

#main(room, furniture)
onTop(room, q5sol)

