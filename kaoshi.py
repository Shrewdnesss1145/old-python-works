'''n=int(input(''))
print(n+1)'''
c=[]
h=[1,2,3,4,5,6,7,8,9]
ab=[]
cd=[]
N=input('')
if 10>N or n>10000:
    print('请重新输入')
    N=input('')
    for i in N:
        c.append(int(i))
    for i in c:    
        for b in h:
            if b==i:
                ab.append(i)
    if ab[0]>=ab[1]:
        cd.append(ab[1])
    else:
        cd.append(ab[0])

    if ab[2]>=ab[3]:
        cd.append(ab[3])
    else:
        cd.append(ab[2])

    if cd[0]>cd[1]:
        print(cd[1])
    else:
        print(cd[0])


