import re
from itertools import combinations
from math import dist, prod


with open("test.txt", "r") as f:
    NODES = [tuple(map(int,line.strip().split(","))) for line in f.readlines()]
EDGES = sorted(combinations(NODES, 2), key=lambda x: dist(x[0], x[1]))

class DSU:
    def __init__(self, nodes):
        self.n = len(nodes)
        self.parent = {u: u for u in nodes}
        self.size = dict.fromkeys(nodes, 1)

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu != pv:
            if self.size[pu] < self.size[pv]:
                pu, pv = pv, pu
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]
            self.n -= 1


def part_one():
    dsu = DSU(NODES)
    limit = 10 if True else 1000
    for u, v in EDGES[:limit]:
        dsu.union(u, v)
    roots = {dsu.find(u) for u in dsu.parent}
    sizes = sorted(dsu.size[r] for r in roots)
    return prod(sizes[-3:])


def part_two():
    dsu = DSU(NODES)
    for u, v in EDGES:
        dsu.union(u, v)
        if dsu.n == 1:
            return u[0] * v[0]


print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")