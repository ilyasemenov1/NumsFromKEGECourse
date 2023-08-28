# петя - первый
# 2 камня или в 3 раза
# зав <= 45 - две кучи
# 1 ход: k>=1, s>=1, k+s<=43

def win(k, s, m):
    if k+s >= 45: return m%2==0
    if m==0: return False
    h=[
        win(k+2, s, m-1),
        win(k*3, s, m-1),
        win(k, s+2, m-1),
        win(k, s*3, m-1),
    ]
    return any(h) if (m-1)%2==0 else all(h)


c=0
for s in range(1, 100):
    for k in range(1, 100):
        if s+k <= 43:
            if win(k, s, 2):
                c+=1

print("1)", c)
print("2)", [
    s 
    for s in range(1, 40) 
    if not win(4, s, 1) and win(4, s, 3)\
    ])
print("3)", [s for s in range(1, 31) if not win(13, s, 2) and win(13, s, 4)])

