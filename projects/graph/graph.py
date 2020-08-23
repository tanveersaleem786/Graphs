"""
Simple graph implementation
"""
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
                print(current_vertex)
                visited_verticies.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    vertices_queue.enqueue(neighbor)
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        vertices_stack = Stack()
        visited_verticies = set()
        vertices_stack.push(starting_vertex)
        while vertices_stack.size() > 0:
            current_vertex = vertices_stack.pop()
            if current_vertex not in visited_verticies:
                print(current_vertex)
                visited_verticies.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    vertices_stack.push(neighbor)
    
    def dft_recursive(self, start_vert, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # keeping track of a visited set of vertices is the "trickiest part"
        # one good solution is to create a optional variable for a visited set you can keep passing around
        if visited is None:
            visited = set()
        visited.add(start_vert)
        print(start_vert)
        # for each neighbor, recurse this function with an updated visited set
        for child_vert in self.vertices[start_vert]:
            if child_vert not in visited:
                self.dft_recursive(child_vert, visited)

        pass  # TODO
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        vertices_queue = Queue()
        visited_verticies = set()
        vertices_queue.enqueue([starting_vertex])
        while vertices_queue.size() > 0:
            current_path = vertices_queue.dequeue()
            if current_path[-1] == destination_vertex:
                return current_path
            if current_path[-1] not in visited_verticies:
                visited_verticies.add(current_path[-1])
                for neighbor in self.get_neighbors(current_path[-1]):
                    vertices_queue.enqueue(current_path + [neighbor])
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        vertices_stack = Stack()
        visited_verticies = set()
        vertices_stack.push([starting_vertex])
        while vertices_stack.size() > 0:
            current_path = vertices_stack.pop()
            if current_path[-1] == destination_vertex:
                return current_path
            if current_path[-1] not in visited_verticies:
                visited_verticies.add(current_path[-1])
                for neighbor in self.get_neighbors(current_path[-1]):
                    vertices_stack.push(current_path + [neighbor])
    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        This should be done using recursion.
        """
        pass  # TODO
if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)
    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    # graph.dft_recursive(1)
    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))
    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
