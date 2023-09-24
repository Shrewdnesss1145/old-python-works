'''a=[]
for i in range(101):
    if i%6==0:
        a.append(i)
print(a)'''


''''b=[]
b.append(2)
b.append(5)
b.append(8)
for i in b:
    for m in b:
        for x in b:
            if x!=m and i!=m and i!=x:
                print(i,m,x,sep=' ')'''



a=[]

'''for i in range(48) :
    m=48-i
    if i*4+m*2==100:
        print(i,m)'''



a=[0,1,2,3]
for i in a:
    for n in a:
        for j in a:
            if j!=n and i!=n and i!=j and i!=0:
                print(i,n,j,sep=' ')
