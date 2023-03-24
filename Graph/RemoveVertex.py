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

    def add_edge(self,v1,v2):
        if v1 in self.adjaceny_list.keys() and v2 in self.adjaceny_list.keys(): # if both the vertices exist only then create the edge
            self.adjaceny_list[v1].append(v2)           #v1 will have v2 inside list and same on v2 vertex scenario
            self.adjaceny_list[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1,v2):
        if v1 in self.adjaceny_list.keys() and v2 in self.adjaceny_list.keys(): 
            self.adjaceny_list[v1].remove(v2)           # we remove edge of v2 from vertex v1 and same for the other scenario
            self.adjaceny_list[v2].remove(v1)
            return True
        return False

    def remove_vertex(self,vertex):
        if vertex in self.adjaceny_list.keys():        # we check if vertex exist in our adjacency list
            for other_vertex in self.adjaceny_list[vertex]:    # we loop through our vertex edges
                self.adjaceny_list[other_vertex].remove(vertex)  # go to each vertex and then remove the edge for the matching vertex
            del self.adjaceny_list[vertex]      # then finally delete the main vertex
            return True
        return False





my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'C')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'D')

my_graph.print_graph()

my_graph.remove_vertex('D')

my_graph.print_graph()