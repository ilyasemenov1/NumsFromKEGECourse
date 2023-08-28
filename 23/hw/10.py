
def f(n, k):
    if n<k: return 0
    if n==k: return 1
    h=[
        f(n-8, k),
        f(n//2, k)
    ]
    return sum(h)

print(f(102, 43)*f(43, 5))