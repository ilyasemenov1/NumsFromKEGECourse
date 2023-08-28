
def f(k, s,d=set()):
    print(s)
    if s==4: d|={k}
    else: 
        f(k+1,s+1,d)
        f(k+5,s+1,d)
        f(k*3,s+1,d)
    return d

print(f(1,2))
