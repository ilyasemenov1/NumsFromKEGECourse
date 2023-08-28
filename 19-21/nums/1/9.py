# три кучи
# петя - 1
# +3 кам. или *2
# >=71
# k1=7 k2=
# 1<=s<=58

def win(k1, k2, k3, m):
    if k1+k2+k3 >= 71: return m%2==0
    if m==0: return False
    h=[
        win(k1+3, k2, k3, m-1),
        win(k1, k2+3, k3, m-1),
        win(k1, k2, k3+3, m-1),
        win(k1*2, k2, k3, m-1),
        win(k1, k2*2, k3, m-1),
        win(k1, k2, k3*2, m-1),
    ]
    return any(h) if (m-1)%2==0 else all(h)

def wins(k1, k2, k3, m):
    if k1+k2+k3 >= 71: return m%2==0
    if m==0: return False
    h=[
        win(k1+3, k2, k3, m-1),
        win(k1, k2+3, k3, m-1),
        win(k1, k2, k3+3, m-1),
        win(k1*2, k2, k3, m-1),
        win(k1, k2*2, k3, m-1),
        win(k1, k2, k3*2, m-1),
    ]
    return any(h)

k1, k2 = 7, 5
print("1)", [s for s in range(1, 59) if wins(k1, k2, s, 2)])
print("2)", [s for s in range(1, 59) if win(k1, k2, s, 3) and not win(k1, k2, s, 1)])
print("3)", [s for s in range(1, 59) if not win(k1, k2, s, 2) and win(k1, k2, s, 4)])
