
def f(n, k):
    if n>k or n==6: return 0
    if n==k: return 1
    h=[
        f(n+2, k),
        f(n*3, k)
    ]
    return sum(h)

print(f(1, 25)*f(25, 63))