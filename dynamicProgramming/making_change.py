import time

def making_change(amount, coins):
    # we want minimum number of coins
    if amount == 0:
        return 0
    min_num_coins = float('inf')
    for coin in coins:
        if amount - coin >= 0:
            num = 1 + making_change(amount - coin, coins)
            min_num_coins = min(num, min_num_coins)

    # if we return infinity, that means no amount of coins can equal
    # the amount. ex) if there are only even coins and we want an odd amount
    return min_num_coins

def making_change_helper(amount, coins, cache):
    if amount <= 0:
        return 0
    if cache[amount] > -1:
        return cache[amount]
    min_num_coins = float('inf')
    for coin in coins:
        if amount - coin >= 0:
            num = 1 + making_change_helper(amount - coin, coins, cache)
            min_num_coins = min(num, min_num_coins)
    cache[amount] = min_num_coins
    return min_num_coins


def making_change_memo(amount, coins):
    if amount <= 0:
        return 0
    cache = [-1] * (amount + 1)
    cache[0] = 0
    making_change_helper(amount, coins, cache)
    return cache[amount]

def making_change_bottom_up(amount, coins):
    if amount <= 0:
        return 0
    cache = [-1] * (amount + 1)
    cache[0] = 0
    for i in range(1, amount + 1):
        min_num_coins = float('infinity')
        for coin in coins:
            if i - coin >= 0:
                num = 1 + cache[i - coin]
                min_num_coins = min(num, min_num_coins)
        cache[i] = min_num_coins

    return cache[amount]

for i in range(2000):
    start = time.time()
    coins = [99, 1]
    # print making_change(i, coins)
    # print making_change_memo(i, coins)
    print making_change_bottom_up(i, coins)
    end = time.time()
    print 'amount =', i, 'num coins =', len(coins), 'and smallest coin =', min(coins)
    print 'took', end-start, 'ms\n'