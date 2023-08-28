
# +1
# *2
# 2->10

def f(n, w):
    if n==10: return 1
    if n>10: return 0
    h=[f(n+1, w), f(n*2, w)]
    return sum(h)

print(f(2, 10))