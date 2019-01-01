# solution 1
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
    