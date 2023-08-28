
# петя ходит первым

def win(s, m):
    if s > 112: return m%2==1
    if s >= 45: return m%2==0
    if m==0: return False
    h=[win(s+2, m-1), win(s*3, m-1)]
    return any(h) if (m-1)%2==0 else all(h)

print(f"1) {[s for s in range(1, 45) if win(s, 2)]}")
print(f"2) {[s for s in range(1, 45) if not win(s, 1) and win(s, 3)]}")
print(f"2) {[s for s in range(1, 45) if win(s, 4) and not win(s, 2)]}")
