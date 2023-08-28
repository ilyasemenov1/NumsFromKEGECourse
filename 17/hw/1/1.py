
import os
path = os.path.join(os.getcwd(), "hw/2")
s=[int(i) for i in open(os.path.join(path, "17_2013.txt"))]
a=[]
for i in s:
    if any(map(lambda x: str(i)[::-1][:1]==str(x), [2, 7])) and all(map(lambda x: i%x==0, [3, 11])):
        a+=[i]
print(len(a), min(a))