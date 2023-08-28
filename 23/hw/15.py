
def to2(n):
    k=""
    while n>0:
        k+=str(n%2)
        n//=2
    return k[::-1]


def f(n, k):
    if int(n,2)>int(k,2) or n==43: return 0
    if n==k: return 1
    h=[
        f(to2(int(n,2)+1), k),
        f(f"{n}0", k),
        f(f"{n}1", k)
    ]
    return sum(h)

print(f("100","11101"))