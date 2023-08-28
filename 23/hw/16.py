
def f(n,k):
    if n>k: return 0
    if n==k: return 1
    h=[f(n+1, k), f(n*1.5, k)] if n%2==0 else [f(n+1, k)]
    return sum(h)

print(f(1,20))