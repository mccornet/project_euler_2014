class magic_5_gon:

    magic_gon = [0]*10 # magic gon squares are filled here

    def print(self):

        # answer is correct but nodes are printed counter clock wise
        n1 = (self.magic_gon[0], self.magic_gon[1], self.magic_gon[2])
        n2 = (self.magic_gon[4], self.magic_gon[3], self.magic_gon[1])
        n3 = (self.magic_gon[6], self.magic_gon[5], self.magic_gon[3])
        n4 = (self.magic_gon[8], self.magic_gon[7], self.magic_gon[5])
        n5 = (self.magic_gon[9], self.magic_gon[2], self.magic_gon[7])

        # correcting clockwise easier than fixing code
        nodes = [n1, n5, n4, n3, n2]
        #print(nodes)

        # From problem description:
        # "Working clockwise, and starting from ...
        # the numerically lowest external node ... "

        # Finding the lowest external value node
        starting_node_v = nodes[0]
        starting_node_i = 0

        for tmp_i in range(1,5) :
            if nodes[tmp_i] < starting_node_v :
                starting_node_i, starting_node_v = tmp_i, nodes[tmp_i]

        sorted_nodes = nodes[starting_node_i:] + nodes[:starting_node_i]

        # extract nodes into string format
        answer = ""
        for node in sorted_nodes :
            for i in range(3) : answer += str(node[i])

        # answer :)
        print("possible solution: ", answer)

    def reset(self):
        for i in range(10):
            self.magic_gon[i] = 0

        # both 16 and 17 character strings possible.
        # only 16 length wanted
        # we need a 10 on the outside!
        self.magic_gon[0] = 10

    def next_empty_field(self):
        for i in range(1,10):
            if self.magic_gon[i] == 0 : return i
        return 0

    def solve(self):
        # 1. find next empty field
        empty_field = self.next_empty_field()

        # 2. no more empty fields: done!
        if empty_field == 0 :
            self.print()
            return True

        # 3. Try all unused values
        for value in range(1,10):

            # 3.0 value still unused
            if value in self.magic_gon : continue

            # 3.1 Fill in value
            self.magic_gon[empty_field] = value

            # 3.2 Check if value possible and solves in recursion
            if self.not_invalid(empty_field): # not invalid

                # try recursion
                res = self.solve()

                # need to find all possibile solutions
                # no exit here when res = True!

            # 3.3 empty value mark
            # self.possible[value] = True

        # 4. If it did not work, empty square and return
        self.magic_gon[empty_field] = 0

        return False

    def not_invalid(self, field):

        if field in [1,3,5,7]:
            return True

        elif field == 2 :
            return (self.magic_gon[0] + self.magic_gon[1] + self.magic_gon[2]) == 14
        elif field == 4 :
            return (self.magic_gon[1] + self.magic_gon[3] + self.magic_gon[4]) == 14
        elif field == 6 :
            return (self.magic_gon[3] + self.magic_gon[5] + self.magic_gon[6]) == 14
        elif field == 8 :
            return (self.magic_gon[5] + self.magic_gon[7] + self.magic_gon[8]) == 14
        elif field == 9 :
            return (self.magic_gon[7] + self.magic_gon[2] + self.magic_gon[9]) == 14
        else:
            return False


mygon = magic_5_gon()
mygon.reset()
mygon.solve()
