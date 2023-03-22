class Graph:
    def __init__(self):
        self.adjaceny_list = {}               # Just create a simple adjaceny empty list

    def print_graph(self):
        for vertex in self.adjaceny_list:
            print(vertex, ":", self.adjaceny_list[vertex])

    def add_vertex(self,vertex):
        if vertex not in self.adjaceny_list.keys():       # we check if the adjaceny list doesnt contain same key
            self.adjaceny_list[vertex] = []              # we create a vertex with empty list
            return True
        return False

my_graph = Graph()
my_graph.add_vertex("A")
my_graph.print_graph()