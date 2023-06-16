class MindGraph:
    def __init__(self):
        self.mind = {}

    def add_cell(self, u, v):
        if u in self.mind:
            self.mind[u].append(v)
        else:
            self.mind[u] = [v]

        if v in self.mind:
            self.mind[v].append(u)
        else:
            self.mind[v] = [u]

    def get_neighbors(self, u):
        if u in self.mind:
            return self.mind[u]
        else:
            return []

# Create an instance
mind = MindGraph()

# Add edges to the graph
mind.add_cell(1, 2)
mind.add_cell(2, 3)
mind.add_cell(3, 4)
mind.add_cell(4, 1)

# Each one of these has its own will.

# Get the neighbors of a vertex
neighbors = mind.get_neighbors(1)
print(neighbors)  # Output: [2, 4]

state={
    1:0,
    2:0,
    3:0,
    4:0
}


