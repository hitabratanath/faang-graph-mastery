import heapq
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, 0, src)]  # (price, stops, node)
        dist = {}

        while heap:
            curr_price, stop, node = heapq.heappop(heap)

            if node == dst:
                return curr_price
            if stop > k:
                continue

            # Avoid revisiting same node with higher stop count
            if (node, stop) in dist and dist[(node, stop)] <= curr_price:
                continue
            dist[(node, stop)] = curr_price

            for nei, price in graph[node]:
                heapq.heappush(heap, (curr_price + price, stop + 1, nei))

        return -1
