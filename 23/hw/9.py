
def f(n, k):
    if n>k: return 0
    if n==k: return 1
    h=[
        f(n+1, k),
        f(n+3, k),
        f(n*2, k)
    ]
    return sum(h)

print(f(3,9)*f(9,12)*f(12,20))