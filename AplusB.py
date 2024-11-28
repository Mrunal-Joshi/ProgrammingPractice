# N = int(input())

# for _ in range(N):
#     a, b = map(int, input().split())
#     print(a + b)

import sys
input = sys.stdin.readline

gi = lambda: list(map(int, input().split(" ")))

N = int(input())

for _ in range(N):
    a, b = gi()
    print(a + b)