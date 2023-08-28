
def win(s: int, m: int) -> bool:
    if s>33: return m%2==0
    if m==0: return False
    h=[
        win(s+1, m-1),
        win(s+2, m-1),
        win(s+3, m-1),
        win(s*2, m-1)
    ]
    return any(h) if (m-1)%2==0 else all(h)

print("1)", [s for s in range(1, 34) if win(s, 2)])
print("2)", [s for s in range(1, 34) if not win(s, 1) and win(s, 3)])
print("3)", [s for s in range(1, 34) if not win(s, 2) and win(s, 4)])

