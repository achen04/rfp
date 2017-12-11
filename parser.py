
def parse(program):
    with open(program) as f:
        line = f.readline()
#        for line in f:
        beg = line.split("#")[0]
        problem_num = beg.split(":")[0]
        room = beg.split(":")[1]
        all_shapes = line.split("#")[1].split(";")
        
        print "Problem", problem_num
        print "Room vertices", room

        for i in range(0, len(all_shapes)):
            shape = all_shapes[i].split(":");
            cost = shape[0];
            vertices = shape[1];
            print i, "Cost is", cost, "for this shape", vertices
            # instead of printing, store into our polygon data structure
            # there are a lot of duplicates so avoid storing duplicates unless
            # intended

program = "input.txt"
parse(program)
