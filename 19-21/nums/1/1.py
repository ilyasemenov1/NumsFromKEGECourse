
def win(s, m):
    if s>=25: return m%2==0
    if m==0: return False
    h=[win(s+2, m-1), win(s*2, m-1)]
    return any(h) if (m-1)%2==0 else all(h)

def min_s():
    for s in range(1, 25):
        if win(s, 2): return s

print([s for s in range(1, 25) if win(s, 2)])
print(len([s for s in range(1, 25) if not win(s, 1) and win(s, 3)]))
print([s for s in range(1, 25) if (win(s, 2) or win(s, 4)) and not win(s, 2)])

