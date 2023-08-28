
def f(k,d=set()):
    if k<100 and k%2==0: d|={k}
    if k<100:
        f(k+3)
        f(k*3)

    return d

print(f(3))
