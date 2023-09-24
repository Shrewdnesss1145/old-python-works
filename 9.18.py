#shrewdness
'''cj=['语文 97','数学 13','英语 36','体育 10','编程 90']
a=[]
for i in cj:
    b=i.split()
    if int(b[1])<60:
        print(b[0],'不及格')'''
    
    
    
'''d = ['东','南','西','北']
r = ['哑巴','喇嘛']
g = ['喇叭','唢呐','榴莲','螺蛳粉']
import random

a=random.randint(0,3)
b=random.randint(0,1)
c=random.randint(0,3)
e=random.randint(1,10)
print('打',d[a],'边来了一个',r[b],'手里提着',e,'斤',g[c])'''



for i in range(1,1001):
    i=str(i)
    if i[::-1]==i:
            n=int(i)
            
            print(n,'是回文数')