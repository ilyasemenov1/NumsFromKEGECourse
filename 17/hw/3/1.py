
import os
path = os.path.join(os.getcwd(), "hw/3")
s=[int(i) for i in open(os.path.join(path, "17_2015.txt"))]
a=[]
for i in s:
    if any(map(lambda x: str(i)[::-1][:1]==str(x), [5,7])) and all(map(lambda x: i%x!=0, [9, 11])):
        a+=[i]
print(len(a), max(a)+min(a))