'''a=int(input('分数:'))
if 0<a or a<59:
    print('不及格')
elif 60<a or a<79:
    print('及格')
elif 80<a or a<89:
    print('良好')
else:
    print('优秀')'''


'''for i in range(0,101):
    print(i)'''
    
    
'''for i in range(0,101,2):
    print(i)'''


'''for i in range(0,101,3):
    print(i)'''


'''a=[]
for i in range(0,101):
    if i%2!=0 and i%3==0:
      a.append(i)  
print(len(a))'''

'''b=[]
import random
for i in range(3):
    b.append(random.randint(1,100))
print(b)'''



'''a=input('5个数字:')
b=eval(a)
print(max(b))
print(b)'''


'''a='303'
c=a.count('3')
print(c)'''


'''dc={'a'=1,'b'=2,'c'=3}
for i,j in dc:
    
print(dc)'''

d=[]
for i in range(1,2021):
    a=str(i)
    c=a.count('2')
    d.append(int(c))
print(sum(d))




