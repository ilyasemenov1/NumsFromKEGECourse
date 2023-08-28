
def win(k1, k2, m):
    if k1+k2>=59: return m%2==0
    if m==0: return False
    h=[
        win(k1+1, k2, m-1),
        win(k1, k2+1, m-1),
        win(k1*2, k2, m-1),
        win(k1, k2*2, m-1),
    ]
    return all(h) if m%2==0 else any(h)

print("1)", [s for s in range(2, 54) if win(5, s, 1)])
print("2)", [s for s in range(2, 54) if not win(5, s, 1) and win(5, s, 3)])
print("2)", [s for s in range(2, 54) if not win(5, s, 2) and win(5, s, 4)])

