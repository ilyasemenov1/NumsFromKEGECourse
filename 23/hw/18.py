
def to3(n):
    k=''
    while n>0:
        k+=str(n%3)
        n//=3
    return k[::-1]

def f(n,s=0,d=set()):
    if s==15: d|={n}
    else: 
        f(to3(int(n,3)*2),s+1,d)
        f(to3(int(n,3)*2+1),s+1,d)
    return d

print(len([int(s,3) for s in f("1")]))