class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """Add edge from v1 to v2."""

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex_id):
        """Breadth-first Traversal."""

        q = Queue()
        q.enqueue(starting_vertex_id)

        visited = set()

        while q.size > 0:
            v = q.dequeue()
            if v not in visited:
                print(v)
                visited.add(v)

                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)
