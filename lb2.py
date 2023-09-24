a=[0,1,2,3]
b=0
for i in a:
    for j in a:
        for q in a:
            if i!=0 and i!=j and j!=q and q!=i:
                print(i,j,q)
                b+=1
print(b)