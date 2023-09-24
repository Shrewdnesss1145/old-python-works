a=eval(input('输入，逗号隔开'))
list=list(a)
n=len(list)
for a in range(n-1):
    for i in range(n-1-a):
        if list[i]<list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
print(list)