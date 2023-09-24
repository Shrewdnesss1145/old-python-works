'''LIST=[]
for i in range(65,91):
    LIST.append(chr(i))
    print(chr(i))
print(LIST)'''
list=[]
a=input('')
for i in a:
    if i=='x':
        print('a',end='')
    elif i=='y':
        print('b',end='')
    elif i=='z':
        print('c',end='')
    else:
        c=chr(ord(i)+3)
        print(c,end='')

