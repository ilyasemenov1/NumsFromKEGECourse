
def f(n, k):
    if n>k or n==43: return 0
    if n==k: return 1
    h=[
        f(n+2, k),
        f(n+n+1, k),
        f(n+n-1, k)
    ]
    return sum(h)

print(f(7,63))