
def win(k1, k2, k3, m):
    if k1+k2+k3>=73: return m%2==0
    if m==0: return False
    h=[
        win(k1+3, k2, k3, m-1),
        win(k1, k2+3, k3, m-1),
        win(k1, k2, k3+3, m-1),
        win(k1+13, k2, k3, m-1),
        win(k1, k2+13, k3, m-1),
        win(k1, k2, k3+13, m-1),
        win(k1+23, k2, k3, m-1),
        win(k1, k2+23, k3, m-1),
        win(k1, k2, k3+23, m-1),
    ]
    return all(h) if m%2==0 else any(h)

def win_any(k1, k2, k3, m):
    if k1+k2+k3>=73: return m%2==0
    if m==0: return False
    h=[
        win(k1+3, k2, k3, m-1),
        win(k1, k2+3, k3, m-1),
        win(k1, k2, k3+3, m-1),
        win(k1+13, k2, k3, m-1),
        win(k1, k2+13, k3, m-1),
        win(k1, k2, k3+13, m-1),
        win(k1+23, k2, k3, m-1),
        win(k1, k2+23, k3, m-1),
        win(k1, k2, k3+23, m-1),
    ]
    return any(h)

k1=2
print("1)", [s for s in range(1, 24) if win_any(2, s, 2*s, 2)])
print("2)", [s for s in range(1, 24) if not win(2, s, 2*s, 1) and win(2, s, 2*s,3)])
print("3)", [s for s in range(1, 24) if not win(2, s, 2*s, 2) and win(2, s, 2*s,4)])

