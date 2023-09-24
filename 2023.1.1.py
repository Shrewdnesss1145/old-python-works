'''a=eval(input('逗号隔开'))
list=list(a)
c=len(list)
for j in range(c-1):
        wz=j
        for i in range(1+j,c):
            if list[wz]>list[i]:
                wz=i
        list[j],list[wz]=list[wz],list[j]
print(list)'''



list=[]
import random
wz=0
a=input('个数')
a=int(a)
for i in range(a):
    d=random.randint(1,100)
    list.append(d)
c=len(list)
for j in range(c-1):
        wz=j
        for i in range(1+j,c):
            if list[wz]>list[i]:
                wz=i
        list[j],list[wz]=list[wz],list[j]
print(list)


