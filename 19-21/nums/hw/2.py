
def win(s: int, m: int) -> bool:
    if s>=60: return m%2==1
    if s>=36: return m%2==0
    if m==0: return False
    h=[
        win(s+1, m-1),
        win(s*2, m-1),
        win(s*3, m-1)
    ]
    return all(h) if m%2==0 else any(h)

print("1)", [
    s
    for s in range(1, 36)
    if win(s, 2)
])
print("2)", [
    s
    for s in range(1, 36)
    if not win(s, 1) and win(s, 3)
])
print("1)", sorted([
    s
    for s in range(1, 36)
    if not win(s, 2) and win(s, 4)
]))