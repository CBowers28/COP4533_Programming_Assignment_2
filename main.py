#input parsing
'''
input example:
3 15
1 2 3 4 1 2 3 4 1 2 3 4 5 1 2
'''
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

def longest_next(cache, future):
    furthest_item = None
    furthest_dist = -1
    for item in cache:
        if item not in future:
            return item
        dist = future.index(item)  # first occurrence
        if dist > furthest_dist:
            furthest_dist = dist
            furthest_item = item
    return furthest_item

def OPTFF(k, m, seq):
    cache = []
    hits = 0
    misses = 0
    for i in range(len(seq)):
        if seq[i] in cache:
            hits += 1
        else:
            misses += 1
            if len(cache) >= k:
                cache.remove(longest_next(cache, seq[i:]))
                cache.append(seq[i])
            else:
                cache.append(seq[i])
    return misses, hits




print(FIFO(k, m, seq))
print(LRU(k, m, seq))
print(OPTFF(k, m, seq))
