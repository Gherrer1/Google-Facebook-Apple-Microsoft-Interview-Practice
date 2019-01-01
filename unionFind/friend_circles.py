# solution 1 - union find
def find(parents, x):
    temp = x
    while parents[temp] != temp:
        temp = parents[temp]
    parents[x] = temp
    return temp

def union(parents, x, y):
    parent1 = find(parents, x)
    parent2 = find(parents, y)
    parents[parent1] = parent2

def find_circle_num(M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    num_students = len(M)
    parents = range(num_students)
    for r, row in enumerate(M):
        for c, val in enumerate(row):
            if val == 1:
                union(parents, r, c)
    circles_set = {}
    for i in range(num_students):
        circle = find(parents, i)
        circles_set[circle] = True
    return len(circles_set)

# solution 2 - dfs
def dfs(visited, index, M):
    visited[index] = 1
    friends = M[index]
    for i, val in enumerate(friends):
        if val == 1 and visited[i] == 0:
            dfs(visited, i, M)

def find_circle_num2(M):
    num_students = len(M)
    visited = [0 for i in range(num_students)]
    circle_count = 0
    for i in range(num_students):
        if visited[i] == 0:
            dfs(visited, i, M)
            circle_count += 1
    return circle_count