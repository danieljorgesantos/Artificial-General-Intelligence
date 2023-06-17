class inputSensoryInformation:
    def __init__(self):
        pass

    def visionPhotoreceptors(self, visionInput):
        pass

    def hearingVibrationCells(self, hearingInput):
        pass

    def abstractInputForTest(self, abstractInput):
        pass

class MindGraph:
    def __init__(self):
        self.mind = {}
        self.state = {}

    # initialize propagation in the mind from inputSensoryInformation changing the state of each cell
    def thalamus(self, entrySignal):
        pass

    # internal management process
    # Creation of new cells
    def neurogenesis(self, u, v):
        if u in self.mind:
            self.mind[u].append(v)
        else:
            self.mind[u] = [v]

        if v in self.mind:
            self.mind[v].append(u)
        else:
            self.mind[v] = [u]

    # internal management process
    def get_neighbors(self, u):
        if u in self.mind:
            return self.mind[u]
        else:
            return []

    # Synaptic plasticity refers to the ability of synapses to change their strength or form new connections.
    # This process is crucial for learning and memory. When two neurons repeatedly activate together,
    # the synapse between them becomes strengthened, making future communication more efficient.
    def synapticPlasticity(self):
        pass

    # checks the state of the cells
    def snapshot(self):
        pass

# Create an instance
mind = MindGraph()

# Add axon (edge) to other cell
mind.neurogenesis(1, 2)
mind.neurogenesis(2, 3)
mind.neurogenesis(3, 4)
mind.neurogenesis(4, 1)

# Each one of these has its own mechanism.

# Get the neighbors of a vertex
neighbors = mind.get_neighbors(1)
print(neighbors)  # Output: [2, 4]

state={
    1:0,
    2:0,
    3:0,
    4:0
}




