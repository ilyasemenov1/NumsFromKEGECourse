
# первый ходит петя

def win(k1, k2, x):
    if k1==k2: return x%2==0
    if x==0: return False
    h=[win(k1+1, k2, x-1) if k1<k2 else win(k1, k2+1, x-1), win(k1+3, k2, x-1) if k1<k2 else win(k1, k2+3, x-1)]
    return any(h) if (x-1)%2==0 else all(h)

def wins(k1, k2, x):
    if k1==k2: return x%2==0
    if x==0: return False
    h=[win(k1+1, k2, x-1) if k1<k2 else win(k1, k2+1, x-1), win(k1+3, k2, x-1) if k1<k2 else win(k1, k2+3, x-1)]
    return any(h)

k1=13

print(f"1) {[s for s in range(1, 24) if win(k1, s, 2)]}")
print(f"2) {[s for s in range(1, 24) if not win(k1, s, 1) and win(k1, s, 3)]}")
print(f"3) {[s for s in range(1, 24) if (not win(k1, s, 2) and win(k1, s, 4))]}")
print(f"3.1) {[s for s in range(1, 24) if wins(k1, s, 2)]}")

# 3) Ans: 7, 19

