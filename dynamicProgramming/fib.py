import time

def fib2(x):
    if x == 0 or x == 1:
        return x
    return fib2(x - 1) + fib2(x - 2)

def fib_helper(x, cache):
    if cache[x] >= 0:
        return cache[x]
    answer = fib_helper(x - 1, cache) + fib_helper(x - 2, cache)
    cache[x] = answer
    return answer

def fib1(x):
    if x < 2:
        return x
    cache = [-1] * (x + 1)
    cache[0] = 0
    cache[1] = 1
    return fib_helper(x, cache)

def fib_bot_up(x):
    if x == 0 or x == 1:
        return x
    cache = [-1] * (x)
    cache[0] = 0
    cache[1] = 1
    for i in range(2, x):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[x - 1] + cache[x - 2]

def fib_optimal(x):
    if x == 0 or x == 1:
        return x
    f1 = 0
    f2 = 1
    for i in range(2, x + 1):
        temp = f1 + f2
        f1 = f2
        f2 = temp
    return f2

for i in range(35):
    start = time.time()
    cache = [-1] * i 
    # print fib_bot_up(i)
    print fib_optimal(i)
    # print fib1(i)
    # print fib2(i)
    end = time.time()
    print i, 'took', end - start, 'ms'

