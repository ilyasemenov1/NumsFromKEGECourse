
def f(n, k):
    if n>k or any(map(lambda x: n==x, [11, 18])): return 0
    if n==k: return 1
    h=[
        f(n+1, k),
        f(n+2, k),
        f(n*3, k)
    ]
    return sum(h)

print(f(4, 8)*f(8, 23))