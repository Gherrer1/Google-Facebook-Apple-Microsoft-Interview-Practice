# 771 on leetcode
def jewels_stones(self, J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    table = {}
    for char in J:
        table[char] = True
    num_jewels = 0
    for char in S:
        if table.get(char):
            num_jewels += 1
    return num_jewels