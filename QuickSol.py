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
room, furniture = parse("input.txt", 8)
shuffle(furniture)

# Find largest x,y for room
largestx = max(room, key=itemgetter(1))[0]
largesty = max(room, key=itemgetter(1))[1]
smallestx = min(room, key=itemgetter(1))[0]
smallesty = min(room, key=itemgetter(1))[1]
room = Polygon(room)
reqArea = room.area * 0.3
currentArea = 0
currentFurniture = []    # Array of polygons already in solution
currentFurnitureNormal = []

# Loop Starts
# Get furniture

for index, itemNormal in enumerate(furniture):

    itemAddAttempt = 0

    while itemAddAttempt < 50:
        itemAddAttempt += 1

        item = Polygon(itemNormal[:-1])  # Convert to polygon
        print("NEW FURNITURE", item)

        # Randomly translate furniture in max room range
        largestFurnx = item.bounds[2]
        largestFurny = item.bounds[3]

        translatex = uniform(smallestx, largestx)
        translatey = uniform(smallesty, largesty)

        print("Translation by: ", translatex, translatey)

        item = translate(item, translatex, translatey)
        print("Translated item", item)

        angle = 0
        while angle <= 360:

            item = rotate(item, 22.5)
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
                    currentArea += item.area
                    print("Added furniture, Area: ", item.area)
                    itemAddAttempt += 1000
                    break

            else:
                print("ITEM NOT IN SHAPE")
            angle += 90

        # Check if area over 30%
        if currentArea > reqArea:
            print("###### Done:\nCurrent Area: ", currentArea, " Required Area: ", reqArea, "Total Shapes: ", len(currentFurniture), "Total Shapes Attempted: ", index)

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

            quit()


print("\n\nEnd")

for i in currentFurniture:
    currentFurnitureNormal.append(list(zip(*i.exterior.coords.xy))[:-1])

print("Items: ", currentFurnitureNormal)
