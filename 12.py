import random
import turtle
'''a=[]
for i in range(65,91):
    a.append(chr(i))
for i in range(97,123):
    a.append(chr(i))
for i in range(4):
    b=random.choice(a)
    print(b,end='')'''
'''a=[]  
for i in range(1001):
    a.append(random.randint(1,10))
for i in range(11):
    print(i,'一共出现了',a.count(i),'次','概率是',a.count(i)/10,'%')'''
'''C=[]
a=input('speak:')
b=list(a)
for i in b:
   if i not in C:
       C.append(i)
print(C)'''


list=[{"姓名":"曹操","一月":539,"二月":720,"三月":662},
      {"姓名":"吕布","一月":678,"二月":490,"三月":810},
      {"姓名":"关羽","一月":952,"二月":616,"三月":574},
      {"姓名":"董卓","一月":296,"二月":848,"三月":879},
      {"姓名":"赵云","一月":1047,"二月":840,"三月":289}]
for i in range(5):
    b=list[i]
    b['总和']=b['一月']+b['二月']+b['三月']
print(list)