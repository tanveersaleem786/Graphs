from util import Stack, Queue  # These may come in handy
class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

        
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            print(f"{v1} doesn't exist")
            return
        if v2 not in self.vertices:
            print(f"{v2} doesn't exist")
            return
        self.vertices[v1].add(v2)
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        return None
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        vertices_queue = Queue()
        visited_verticies = set()
        vertices_queue.enqueue(starting_vertex)              
        while vertices_queue.size() > 0:
            current_vertex = vertices_queue.dequeue()
            if current_vertex not in visited_verticies:
                #print(current_vertex)
                visited_verticies.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    vertices_queue.enqueue(neighbor)
        #print(current_vertex)
        if current_vertex ==  starting_vertex:
            return -1
        return current_vertex

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()  # Instantiate your graph   
    for anc in ancestors:
        graph.add_vertex(anc[0])
        graph.add_vertex(anc[1])
        graph.add_edge(anc[1], anc[0])
    
    return graph.bft(starting_node)
    
    # for anc in ancestors:
    #     print('{} : {}'.format(anc[0], anc[1]))


ancestors =  [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 8))