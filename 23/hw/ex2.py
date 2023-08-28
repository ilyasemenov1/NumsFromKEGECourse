
def f(n,k,c=0):
    if n>k: return 0
    if n==k and c==2: return 1
    h=[
        f(n+1, k, 1),
        f(n+2, k, 2)
    ]
    return sum(h)

print(f(3,19))