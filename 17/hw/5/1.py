
import os
path = os.path.join(os.getcwd(), "hw/1")
s=[int(i) for i in open(os.path.join(path, "17_2003.txt"))]
a=[]
for i in s:
    if i%3==0 and all(map(lambda x: i%x!=0, [7, 17, 19, 27])):
        a+=[i]
print(len(a), max(a))