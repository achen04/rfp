import ast


def parse(program):
    with open(program) as f:
        line = f.readline()

#        for line in f:
        beg = line.split("#")[0]
        problem_num = beg.split(":")[0]
        room = beg.split(":")[1]
        all_shapes = line.split("#")[1].split(";")
        
        print("Problem", problem_num)
        print("Room vertices", room)

        for i in range(0, len(all_shapes)):
            shape = all_shapes[i].split(":")
            cost = shape[0] # think about how cost will be stored in the list
            vertices = shape[1]
            arr_tuples = ast.literal_eval("[{}]".format(vertices))
            print(i, "Cost is", cost, "for this shape", arr_tuples)


program = "input.txt"
parse(program)
