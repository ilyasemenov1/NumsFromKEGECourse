
# первым ходит петя

def win(k1, k2, x):
    if k1+k2 >= 45: return x%2==0
    if x==0: return False
    h=[win(k1+1, k2, x-1), win(k1, k2+1, x-1), win(k1*3, k2, x-1), win(k1, k2*3, x-1)]
    return any(h) if (x-1)%2==0 else all(h)

def wins(k1, k2, x):
    if k1+k2 >= 45: return x%2==0
    if x==0: return False
    h=[win(k1+1, k2, x-1), win(k1, k2+1, x-1), win(k1*3, k2, x-1), win(k1, k2*3, x-1)]
    return any(h)

k1=4
print(f"1) {[k2 for k2 in range(1, 41) if wins(k1, k2, 2)]}")
print(f"2) {[k2 for k2 in range(1, 41) if not win(k1, k2, 1) and win(k1, k2, 3)]}")
print(f"3) {[k2 for k2 in range(1, 41) if not win(k1, k2, 2) and win(k1, k2, 4)]}")

 