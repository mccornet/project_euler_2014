class Vertex:
 
    def __init__(self, m, n):
        self.values = [m, n]
        self.children = (
            [(2*m)-n, m],
            [(2*m)+n, m],
            [m+(2*n), n]
        )
 
def generate_coprimes():
    vertices = [Vertex(15, 1), Vertex(11, 1)]
    iteration = 0
    while True:
        iteration += 1
        print('Iteration #{}'.format(iteration))
        new_vertices = []
        for v in vertices:
            for c in v.children:
                print(c)
                new_vertices.append(Vertex(*c))
        vertices = new_vertices
        input()
 
if __name__ == '__main__':
    generate_coprimes()