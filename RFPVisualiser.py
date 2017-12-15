from graphics import *
from operator import itemgetter
from random import randint
import ast

AXIS_X = 1000
AXIS_Y = 700
SCALE = 80

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
    display.setFill(color_rgb(0, 134, 244))
    display.draw(win)

    win.getMouse()
    win.close()


def onTop(room, furniture):
    win = GraphWin("Visualiser", AXIS_X, AXIS_Y)
    win.setBackground(color_rgb(0, 0, 0))

    # Room
    roomPoints = []

    for coord in room:
        roomPoints.append(Point(coord[0] * SCALE + 300, coord[1] * SCALE + 300))

    display = Polygon(roomPoints)
    display.setFill(color_rgb(66, 134, 244))
    display.draw(win)

    # Furniture
    for index, furniture in enumerate(furniture):
        furniturePoints = []

        for coord in furniture[:-1]:
            furniturePoints.append(Point(coord[0] * SCALE + 300, coord[1] * SCALE + 300))

        weight = round(furniture[-1][1]*3)

        display = Polygon(furniturePoints)
        display.setFill(color_rgb(255, 20, 100))
        display.draw(win)

    win.getMouse()
    win.close()

q5sol = [[(0.1574946260997432, 0.990114135149467), (-0.2755405275414931, 1.017237091875164), (-0.3026634842671902, 0.5842019382339277), (0.1303716693740461, 0.5570789815082305)], [(0.36543129412783837, 1.5916653777452185), (-0.06259601033790013, 1.5206180294313851), (0.00845133797593317, 1.0925907249656468), (0.4364786424416719, 1.16363807327948)], [(0.7935001218540325, 1.3513270710851724), (0.15701009061037097, 0.7614958779375263), (0.7468412837580174, 0.12500584669386472), (1.383331315001678, 0.7148370398415105)], [(0.4979721168093284, 0.2814297932501684), (0.24874453195974794, 0.6365927277192347), (-0.10641840250931847, 0.3873651428696543), (0.14280918234026202, 0.03220220840058792)]]

room, furniture = parse("input.txt", 5)

#main(room, furniture)
onTop(room, q5sol)

