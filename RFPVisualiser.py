from graphics import *
from operator import itemgetter
from random import randint
import ast

AXIS_X = 1000
AXIS_Y = 700
SCALE = 20

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

q5sol = [[(0.658184340470968, 1.4279926631552122), (-0.10927736506497493, 1.0229952226467633), (0.29572007544347445, 0.2555335171108204), (1.0631817809794164, 0.6605309576192693), (0.658184340470968, 1.4279926631552122)], [(0.21022554714773461, 1.3011041369641263), (-0.0503968588236921, 1.6479918141397474), (-0.39728453599931335, 1.3873694081683206), (-0.13666213002788663, 1.0404817309926995), (0.21022554714773461, 1.3011041369641263)]]


q3sol = [[(0.0, 0.0), (5.0, 0.0), (6.0, 4.0), (-2.0, 4.0), (0.0, 0.0)]]

q13sol = [[(4.37955986726222, 8.023159365777781), (6.371034049206023, 7.135218921084113), (7.25897449389969, 9.126693103027918), (5.267500311955886, 10.014633547721585)], [(9.874475327065886, 13.597852124904861), (7.757161360249988, 14.118802426371186), (7.236211058783662, 12.00148845955529), (9.353525025599561, 11.480538158088963)], [(9.284582342615872, 16.28657062898862), (10.267539349598815, 14.340239934298054), (12.213870044289381, 15.323196941280996), (11.230913037306438, 17.269527635971563)], [(5.085884398751204, 11.264715292093737), (7.678121823432698, 9.754647368429158), (8.181477797987558, 10.618726509989655), (5.589240373306063, 12.128794433654235)], [(4.523717236075501, 10.794512901329522), (3.1111669085542895, 8.14787322577493), (3.9933801337391532, 7.677023116601193), (5.405930461260365, 10.323662792155785)], [(8.191874176149794, 14.841390847136134), (8.898772804053257, 14.858546891791017), (9.984854812890777, 13.823933016918145), (10.00201085754566, 13.117034389014682), (10.69175344079424, 13.841089061573028), (8.881616759398375, 15.565445519694482)], [(1.1132819056741072, 6.778179379291613), (1.7452574027119074, 6.0031910108990125), (2.5202457711045083, 6.6351665079368125), (1.8882702740667077, 7.410154876329414)], [(2.9665360213208314, 1.6388805291814093), (1.9691413794094224, 1.5667422710487644), (2.0412796375420674, 0.5693476291373551), (3.0386742794534767, 0.6414858872700002)], [(1.814199008208306, 4.336040500798683), (1.9681249129607477, 3.347958107550963), (2.956207306208468, 3.5018840123034045), (2.802281401456026, 4.489966405551125)], [(6.046215182591479, 11.91875584943144), (7.023387407224393, 11.706307165260505), (7.235836091395328, 12.68347938989342), (6.258663866762413, 12.895928074064354)], [(1.493639780039826, 0.14521521048558939), (0.6865660215329149, -0.44523542109128356), (1.277016653109787, -1.2523091795981944), (2.084090411616699, -0.6618585480213215)], [(9.223278342351268, 11.239625878275397), (8.34356729844307, 11.715134531431099), (7.868058645287369, 10.8354234875229), (8.747769689195566, 10.3599148343672)], [(4.773313105565357, 0.2669859588522492), (3.7733141470551654, 0.2684292116129613), (3.771870894294453, -0.7315697468972308), (4.771869852804645, -0.7330129996579429)], [(2.364766091723367, 9.476326022630515), (1.6614964418318925, 10.18724922491155), (0.9505732395508564, 9.483979575020076), (1.6538428894423312, 8.77305637273904)]]


room, furniture = parse("input.txt", 13)

#main(room, furniture)
onTop(room, q13sol)

