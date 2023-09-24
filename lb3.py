a=input('输入多个正整数，用空格隔开')
b=a.split()
print(b)
list_num=[]
for i in b:
     if int(i)%2 == 0:
         list_num.append(int(i))
print(list_num)
n=max(list_num)+1
bucket=[0]*n
for i in list_num:
    bucket[i]+=1
    list_num2=[]
    for i in range(len(bucket)-1,-1,-1):
        if bucket[i]!=0:
            for j in range(bucket[i]):
                list_num2.append(i)
print(list_num2)