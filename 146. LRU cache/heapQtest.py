import heapq

a = []
heapq.heappush(a,1)
heapq.heappush(a,3)
heapq.heappush(a,7)
heapq.heappush(a,8)
heapq.heappush(a,9)


c = heapq.heappop(a)
print(c)
