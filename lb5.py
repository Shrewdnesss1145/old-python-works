a=list(map(int,input('任意输入高度').split(',')))
print(a)
b=0
while True:
     a.sort()
     for i in range(len(a)-1):
         a[i]+=1
     print(a)
     b+=1
     if max(a) == min (a):
         break
print(b)