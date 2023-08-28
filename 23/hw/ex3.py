
from functools import lru_cache

@lru_cache(None)
def f(n,k,s=0):
    if n>k: return 10**10
    if n==k: return s
    h=[
        f(n+1,k,s+1),
        f(n+5,k,s+1),
        f(n*3,k,s+1)
    ]
    return min(h)

print(f(1,227))