#input parsing
k, m = map(int, input().split())
seq = list(map(int, input().split()))



def FIFO(k, m, seq):
    cache = []
    hits = 0
    misses = 0
    for num in seq:
        if num in cache:
            hits += 1
        else:
            misses += 1
            if len(cache) >= k:
                cache.pop(0)
                cache.append(num)
            else:
                cache.append(num)

    return misses, hits

def LRU(k, m, seq):
    cache = []
    hits = 0
    misses = 0
    for num in seq:
        if num in cache:
            hits += 1
            cache.remove(num)
            cache.append(num)
        else:
            misses += 1
            if len(cache) >= k:
                cache.pop(0)
                cache.append(num)
            else:
                cache.append(num)
    return misses, hits


print(FIFO(k, m, seq))
print(LRU(k, m, seq))

