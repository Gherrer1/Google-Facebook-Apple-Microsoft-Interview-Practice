
def find(mapping, node):
    while mapping[node] != node:
        node = mapping[node]
    return node

def union(mapping, source, dest):
    parent1 = find(mapping, source)
    parent2 = find(mapping, dest)
    if parent1 != parent2:
        mapping[parent1] = parent2


N = input()
mapping = [i for i in range(2 * N + 1) ]
for i in range(N):
    (source, dest) = [ int(x) for x in raw_input().split() ]
    union(mapping, source, dest)
set_sizes = {}
for node in range(1, 2*N + 1):
    parent = find(mapping, node)
    set_sizes[parent] = set_sizes.get(parent, 0) + 1

eligible_sizes = [x for x in set_sizes.values() if x > 1]
print min(eligible_sizes), max(eligible_sizes)
