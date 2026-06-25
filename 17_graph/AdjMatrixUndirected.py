class AdjMatrixUndirected:

    def __init__(self, n):
        self.n = n
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def display(self):
        for row in self.matrix:
            print(*row)


n = int(input("Enter number of vertices: "))

g = AdjMatrixUndirected(n)

while True:
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

    ch = int(input("Enter -1 to stop else 0: "))

    if ch == -1:
        break

print("\nAdjacency Matrix")

g.display()
