'''a=[12,46,94,56,21,6,12,31,26]
b=0
for i in a:
    b=b+1
    if i==26:
        print('have')
        print('第',b,'个')
        break
else:
    print('无')'''

'''list=[12,46,94,56,21,6,12,31,26]
list.sort()
key=26
ks=0
js=len(list)-1
while ks<=js:
    z=(ks+js)//2
    if key>list[z]:
        ks=z+1
    elif key<list[z]:
        ks=z-1
    else:
        print('在',(z+1),'个')
        break
else:
    print('no')'''
import random
a=[]
for i in range(10):
    a.append(random.randint(0,100))
a.sort()
b=input('整数a')
key=int(b)
ks=0
js=len(a)-1
while ks<=js:
    z=(ks+js)//2
    if key>a[z]:
        ks=z+1
    elif key<a[z]:
        js=z-1
    else:
        print('在',(z+1),'个')
        break
else:
    print('no')