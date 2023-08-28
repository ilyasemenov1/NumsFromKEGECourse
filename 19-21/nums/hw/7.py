
def win(k1, k2, m):
    if k1*k2>=63: return m%2==0
    if m==0: return False
    h=[
        win(k1+1, k2, m-1),
        win(k1, k2+1, m-1),
        win(k1*2, k2, m-1),
        win(k1, k2*2, m-1)
    ]
    return all(h) if m%2==0 else any(h)

k1=2
print("1)", [s for s in range(1, 32) if not win(k1, s, 1) and win(k1, s, 2)])
print("2)", [s for s in range(1, 32) if not win(k1, s, 1) and win(k1, s, 3)])
print("3)", [s for s in range(1, 32) if not win(k1, s, 2) and win(k1, s, 4)])
