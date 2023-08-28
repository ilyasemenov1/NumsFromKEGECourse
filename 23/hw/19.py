
def f(n,s=0,d=set()):
    if s==8: d|={n}
    else:
        f(n+1,s+1)
        f(n+5,s+1)
        f(n*3,s+1)
    return d

print([i for i in f(1) if i>=1000 and i<=1024])