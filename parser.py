import ast


def parse(program):
    arr_tuples = []
    with open(program) as f:
        line = f.readline()

#        for line in f:
        beg = line.split("#")[0]
        problem_num = beg.split(":")[0]
        global room 
        room = ast.literal_eval("[{}]".format(beg.split(":")[1]))
        all_shapes = line.split("#")[1].split(";")
        
        print("Problem", problem_num)
        print("Room vertices", room)

        for i in range(0, len(all_shapes)):
            shape = all_shapes[i].split(":")
            cost = shape[0] # think about how cost will be stored in the list
            vertices = shape[1]
            arr_tuples += [ast.literal_eval("[{}]".format(vertices))]
            print(i, "Cost is", cost, "for this shape", vertices)
    return arr_tuples

def find_area(vertices):
    area = 0.0
    for i in range(len(vertices)):
        if (i + 1 < len(vertices)):
            # all values casted to float
            area += ((float)(vertices[i][0])*(float)(vertices[i+1][1])) - ((float)(vertices[i][1])*(float)(vertices[i+1][0]))
    area = area / 2
    return area

program = "input.txt"
global room
all_furniture = parse(program)
print(all_furniture)
area = find_area(all_furniture[0])
print("HERE IS THE AREA", area)
room_area = find_area(room)
print("HERE IS THE ROOM AREA", room_area)

