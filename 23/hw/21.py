
def f(n,k,c=1):
    if n>k: return 0
    if n==k: return 1
    h=[f(n+1, k, 1),f(n+2, k, 1),f(n*2, k, 2)] if c!=2 else [f(n+1, k, 2),f(n+2, k, 2)]
    return sum(h)

print(f(2,12))