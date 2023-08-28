
def win(k, m):
    if k>=2163: return m%2==0
    if m==0: return False
    h=[
        win(k+1, m-1),
        win(k*3, m-1)
    ]
    return all(h) if m%2==0 else any(h)

print("1)", [s for s in range(1, 2163) if not win(s, 1) and win(s, 2)])
print("2)", [s for s in range(1, 2163) if not win(s, 1) and win(s, 3)])
print("3)", [s for s in range(1, 2163) if not win(s, 2) and win(s, 4)])
