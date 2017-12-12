import ast
import math
from shapely.geometry import Point, LineString, Polygon
from shapely import affinity
from pprint import pprint

def parse(program):
    arr_tuples = []
    with open(program) as f:
        line = f.readline()
#        for line in f:
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
   

# idenitifies orientation of the points (counterclockwise check)
def ccw(A, B, C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect_A(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
    #return ((ccw(A, B, C) * ccw(A, B, D)) <= 0) and ((ccw(C, D, A) * ccw(C, D, B)) <= 0)

def intersect(A, B, C, D):
    xdiff = (A[0] - B[0], C[0] - D[0])
    ydiff = (A[1] - B[1], C[1] - D[1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False

    d = (det(A, B), det(C, D))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    print("intersect", x, y)

# makes the room and list of furnitures into polygon object
def poly(room, furniture):
    room_p = Polygon(room)
    furn_p = [Polygon(f[:-1]) for f in furniture]

    return room_p, furn_p

def poly_intersect(room_p, one_furniture_p):
    return (one_furniture_p.intersects(room_p))


# if there's a diff, will evaluate to false and returns the vertices differences
# if no diff, returns false
def poly_diff(p1, p2):
    return (p1.difference(p2))

# returns true if the whole obj contains the other and 
# returns false if not entirely containing
def poly_contains(p1, p2):
    return (p1.contains(p2))
    
def place_furniture(room_o_p, room_p, furniture_p, placed_p):
    for i in range(0, len(furniture_p)): # change back to len(furniture_p) later
        if (poly_contains(room_p, furniture_p[i])): 
            # change the room size by subtracting, but think of cases of the hole
            new_room_p = poly_diff(room_p, furniture_p[i])
            placed_p.append(furniture_p[i])
            if (new_room_p.area > (0.3*room_o_p.area)):
                #print("original area",  room_o_p.area)
                #print("our new area is", new_room_p.area)
                placed_p = format_poly_to_tuples(placed_p) #formatting not right
                #print("placed furniture is", placed_p)
                return placed_p
            else:
                place_furniture(room_o_p, new_room_p, furniture_p, placed_p)
            
        # else, rotate and translate until it fits/check the length of the side can still fit in room

def format_poly_to_tuples(poly_list):
    output = []
    for i in range(0, len(poly_list)):
        output += list(poly_list[i].exterior.coords)
    return output

def dot(vA, vB):
    return vA[0]*vB[0]+vA[1]*vB[1]

def findAngleToRotate(lineA, lineB):
    # Get nicer vector form
    vA = [(lineA[0][0]-lineA[1][0]), (lineA[0][1]-lineA[1][1])]
    vB = [(lineB[0][0]-lineB[1][0]), (lineB[0][1]-lineB[1][1])]
    # Get dot prod
    dot_prod = dot(vA, vB)
    # Get magnitudes
    magA = dot(vA, vA)**0.5
    magB = dot(vB, vB)**0.5
    # Get cosine value
    cos_ = dot_prod/magA/magB
    # Get angle in radians and then convert to degrees
    angle = math.acos(dot_prod/magB/magA)
    # Basically doing angle <- angle mod 360
    ang_deg = math.degrees(angle)%360

    if ang_deg-180>=0:
        # As in if statement
        return 360 - ang_deg
    else:
        return ang_deg

def rotatePolgyon(p, degree):
    return affinity.rotate(p, degree, origin='centroid')

def find_longest_side(p):
    pass
        
program = "input.txt"
room, all_furniture = parse(program)
room_p, furniture_p = poly(room, all_furniture)
place_furniture(room_p, room_p, furniture_p, [])
print(room_p)
print(furniture_p[4])



