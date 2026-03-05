import sys
import bisect
from collections import deque, OrderedDict, defaultdict


def parse_input(filepath):
    with open(filepath) as f:
        tokens = f.read().split()
    k = int(tokens[0])
    m = int(tokens[1])
    requests = list(map(int, tokens[2:2 + m]))
    return k, m, requests


def fifo(k, requests):
    cache = set()
    order = deque()
    misses = 0

    for req in requests:
        if req in cache:
            continue
        misses += 1
        if len(cache) == k:
            cache.remove(order.popleft())
        cache.add(req)
        order.append(req)

    return misses


def lru(k, requests):
    cache = OrderedDict()
    misses = 0

    for req in requests:
        if req in cache:
            cache.move_to_end(req)
            continue
        misses += 1
        if len(cache) == k:
            cache.popitem(last=False)
        cache[req] = True

    return misses


def optff(k, requests):
    positions = defaultdict(list)
    for i, r in enumerate(requests):
        positions[r].append(i)

    def next_occurrence(item, after):
        lst = positions[item]
        idx = bisect.bisect_right(lst, after)
        return lst[idx] if idx < len(lst) else float('inf')

    cache = set()
    misses = 0

    for i, req in enumerate(requests):
        if req in cache:
            continue
        misses += 1
        if len(cache) == k:
            cache.remove(max(cache, key=lambda x: next_occurrence(x, i)))
        cache.add(req)

    return misses


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    k, m, requests = parse_input(sys.argv[1])

    print(f"FIFO  : {fifo(k, requests)}")
    print(f"LRU   : {lru(k, requests)}")
    print(f"OPTFF : {optff(k, requests)}")


if __name__ == "__main__":
    main()