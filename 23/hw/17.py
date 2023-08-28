
from functools import lru_cache

@lru_cache
def f(n,k):
    if n>k: return 0
    if n==k: return 1
    h=[
        f(n+2, k),
        f(n+4, k),
        f(n+5, k)
    ]
    return sum(h)


for i in range(32, 100):
    if f(31, i) == 1001:
        print(i)
        break