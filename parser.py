import ast
from shapely.geometry import Point, LineString, Polygon
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
'''
def place_furniture(all_furniture):
    global room 
    f = all_furniture[0]
    print ("room is", room)
    print ("furniture is", f)
    # check for intersection on all sides of the furniture
    # number of vertices = number of sides
    for i in range(len(f)-1): # -1 because last one is not a vertex, but (cost, area)
        if (i + 1 < (len(f) - 1)):
            for j in range(len(room)):
                if (j + 1 < len(room)):
                    if (intersect(room[j], room[j+1], f[i], f[i+1])):
                        print("intersected", room[j], room[j+1], f[i], f[i+1])
                    else: 
                        print("no intersect", room[j], room[j+1], f[i], f[i+1])
                else:
                    if (intersect(room[j], room[0], f[i], f[i+1])):
                        print("intersected", room[j], room[0], f[i], f[i+1])
                    else:
                        print("no intersect", room[j], room[0], f[i], f[i+1])
        else:
             for j in range(len(room)):
                if (j + 1 < len(room)):
                    if (intersect(room[j], room[j+1], f[-2], f[0])):
                        print("intersected", room[j], room[j+1], f[-2], f[0])
                    else: 
                        print("no intersect", room[j], room[j+1], f[-2], f[0])
                else:
                    if (intersect(room[j], room[0], f[-2], f[0])):
                        print("intersected", room[j], room[0], f[-2], f[0])
                    else:
                        print("no intersect", room[j], room[0], f[-2], f[0])
'''         
    
    

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
    for i in range(0, 1): # change back to len(furniture_p) later
        if (poly_contains(room_p, furniture_p[i])): 
            # change the room size by subtracting, but think of cases of the hole
            new_room_p = poly_diff(room_p, furniture_p[i])
            placed_p.append(furniture_p[i])
            if (new_room_p.area > (0.3*room_o_p.area)):
                print("our new area is", new_room_p.area)
                format_poly_to_tuples(placed_p)
                print("placed furniture is", placed_p[0])
            '''
            else:
                place_furniture(room_o_p, new_room_p, furniture_p)
            '''
        # else, rotate and translate until it fits/check the length of the side can still fit in room
    print(new_room_p)

def format_poly_to_tuples(poly_list):
    output = []
    for i in range(0, len(poly_list)):
        output += ast.literal_eval("[{}]".format(poly_list[i]))
    print(output)



program = "input.txt"
room, all_furniture = parse(program)
print(room)
print(all_furniture)
room_p, furniture_p = poly(room, all_furniture)
place_furniture(room_p, room_p, furniture_p, [])
