from operator import itemgetter
from shapely.geometry import *
from shapely.affinity import *
import ast
from random import randint, uniform, shuffle


def parse(program, question):
    def find_area(vertices):
        area = 0.0
        for i in range(len(vertices)):
            if (i + 1 < len(vertices)):
                # all values casted to float
                area += ((float)(vertices[i][0]) * (float)(vertices[i + 1][1])) - (
                        (float)(vertices[i][1]) * (float)(vertices[i + 1][0]))
        area += ((float)(vertices[-1][0]) * (float)(vertices[0][1])) - (
                (float)(vertices[-1][0]) * (float)(vertices[0][1]))
        area = area / 2
        return area

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

# Add shapes to random position
def checkIntersect(room, furniture):
    return room.intersects(furniture)


# GET INPUTS
room, furniture = parse("input.txt", 5)
print(furniture)
furniture.sort(key=lambda x: x[-1][-1], reverse=True)
print(furniture)


# Find largest x,y for room
room = Polygon(room)

largestx2 = room.bounds[2]
largesty2 = room.bounds[3]
smallestx2 = room.bounds[0]
smallesty2 = room.bounds[1]

print(largestx2, largesty2, smallestx2, smallesty2)

reqArea = room.area * 0.3
currentArea, weight = 0, 0
currentFurniture = []    # Array of polygons already in solution
currentFurnitureNormal = []

# Loop Starts
# Get furniture

for index, itemNormal in enumerate(furniture):

    itemAddAttempt = 0

    while itemAddAttempt < 750:
        itemAddAttempt += 1

        item = Polygon(itemNormal[:-1])  # Convert to polygon
        print("NEW FURNITURE", item)

        translatex = uniform(smallestx2, abs(largestx2*2))
        translatey = uniform(smallesty2*2, largesty2*2)

        print("Translation by: ", translatex, translatey)

        item = translate(item, translatex, translatey)
        print("Translated item", item)

        angle = 0
        while angle <= 360:

            item = rotate(item, 15)
            print("Rotated: ", item)

            # Check furniture fits inside room
            if room.contains(item):

                # Check new furniture not inside currentFurniture
                intersect = False
                for furniture in currentFurniture:
                    if checkIntersect(furniture, item):
                        intersect = True
                        print("FURNITURE INTERSECTS CURRENT")
                        print("Current Furn: ", furniture)
                        break

                # Add furniture to currentFurniture
                if intersect == False:
                    currentFurniture.append(item)
                    weight += itemNormal[-1][0]*itemNormal[-1][1]
                    currentArea += item.area
                    print("+++++++++++++++++++++++Added furniture++++++++++++++++++++++++++++")
                    itemAddAttempt += 1000
                    break

            else:
                print("ITEM NOT IN SHAPE")
                angle += 360
            angle += 15

        # Check if area over 30%
        if currentArea > reqArea:
            print("###### Done:\nCurrent Area: ", currentArea, "Area %: ", currentArea*100/room.area, "Weight: ", weight,
                   "Total Shapes: ", len(currentFurniture), "Total Shapes Attempted: ", index+1)


for i in currentFurniture:
    currentFurnitureNormal.append(list(zip(*i.exterior.coords.xy))[:-1])

print(currentFurnitureNormal)

for index, i in enumerate(currentFurnitureNormal):
    for index2, j in enumerate(i):
        if index2 == len(i) - 1:
            print("(" + str(j[0]) + ", " + str(j[1]) + ")" , end="")
        else:
            print("(" + str(j[0]) + ", " + str(j[1]) + "), " , end="")

    if index != len(currentFurnitureNormal)-1:
        print(";", end=" ")

print("\n\nEnd")

for i in currentFurniture:
    currentFurnitureNormal.append(list(zip(*i.exterior.coords.xy))[:-1])

print("Failed Items:\n ", currentFurnitureNormal)
