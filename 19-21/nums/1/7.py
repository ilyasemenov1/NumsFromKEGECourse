
# первым ходит петя

def win(k, x):
    if k >= 41: return x%2==0
    if x==0: return False
    h=[win(k+1, x-1)]
    if k*2 <= 50: h+=[win(k*2, x-1)]
    if k<= 48: h+=[win(k+2, x-1)]
    
    return any(h) if (x-1)%2==0 else all(h)

print("1)", [s for s in range(1, 41) if win(s, 4) and not win(s, 2)])
print("2)", [s for s in range(1, 41) if win(s, 6) and not (win(s, 2) or win(s, 4))])
print("3)", [s for s in range(1, 41) if not win(s, 1) and win(s, 3)])

print("3)", [s for s in range(1, 41) if not win(s, 0) and win(s, 2)])

# 3 Ans: 19