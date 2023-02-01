import heapq
from heapq import heappush, heappop, heapify
import sys
input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    number = int(input())
    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, number)
