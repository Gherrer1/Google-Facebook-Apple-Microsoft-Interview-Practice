class UnionFind(object):
    def __init__(self, num_nodes):
        self.parent = range(num_nodes + 1)

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def is_redundant(self, x, y):
        parent1 = self.parent[x]
        parent2 = self.parent[y]
        if parent1 == parent2:
            return True
        return False

    def union(self, x, y):
        parent1 = self.parent[x]
        parent2 = self.parent[y]
        self.parent[parent1] = parent2

def find_redundant_connection(edges):
    """
    :type edges: List[List[int]]
    :rtype List[int]
    """
    num_vertices = len(edges)
    dsj = UnionFind(num_vertices)
    for x, y in edges:
        if dsj.is_redundant(x, y):
            return [x, y]
        dsj.union(x, y)