
# первым ходит петя

def win(k1, k2, x):
    if k1+k2 <= 20: return x%2==0
    if x==0: return False
    h=[win(k1-1, k2, x-1), win(k1, k2-1, x-1), win((k1+1)//2, k2, x-1), win(k1, (k2+1)//2, x-1)]
    return any(h) if (x-1)%2==0 else all(h)

k1=10
print(f"1) {[s for s in range(11, 1000) if win(k1, s, 2)]}")
print(f"1) {[s for s in range(11, 1000) if not win(k1, s, 1) and win(k1, s, 3)]}")
print(f"1) {[s for s in range(11, 1000) if not win(k1, s, 2) and win(k1, s, 4)]}")

