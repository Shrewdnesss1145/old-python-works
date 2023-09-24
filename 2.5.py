
'''def age(n):
    if n==1:
        return 10
    else:
        return age(n-1)+2

def abc(n):
    if n==1 or n==2:
        return 1
    else:
        return abc(n-1)+abc(n-2)
print(abc(10000))'''


a=int(input('几的阶乘'))
def abc(n):
    if n==1:
        return 1
    else:
         return n*abc(n-1)

print(abc(a))

