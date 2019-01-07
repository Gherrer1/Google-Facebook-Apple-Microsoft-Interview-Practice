# 877 on Leetcode
def hash_inputs(start, end):
    return str(start) + str(end)

def pick_piles(piles, start, end, turn, cache):
    if start > end:
        return 0
    
    if cache.get(hash_inputs(start, end)):
        return cache[hash_inputs(start, end)]

    # Alexs turn
    if turn % 2 == 0:
        res = max(
            piles[start] + pick_piles(piles, start + 1, end, turn + 1, cache),
            piles[end] + pick_piles(piles, start, end - 1,  turn + 1, cache)
        )
    # Lee
    else:
        res = min(
            -piles[start] + pick_piles(piles, start + 1, end, turn + 1, cache),
            -piles[end] + pick_piles(piles, start, end - 1, turn + 1, cache)
        )
    cache[hash_inputs(start, end)] = res
    return res

print pick_piles([5, 30, 4, 4], 0, 3, 0, {})