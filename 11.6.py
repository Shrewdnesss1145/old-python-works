'''def 多边形(边长,边数,颜色='red',粗细=5):
    import turtle as t
    t.pencolor(颜色)
    t.pensize(粗细)
    for i in range(边数):
        t.fd(边长)
        t.rt(360/边数)




多边形(200,5,'blue',10)'''

'''def 函数(姓名,年龄,性别="男",地址="北京"):
    print("姓名:",姓名)
    print("年龄:",年龄)
    print("性别:",性别)
    print("地址:",地址)

函数('杨嘉诚',100000000,地址='镇江')'''


'''def 判断及格(*分):
    for i in 分:
        if i>=60:
            print(i,'及格')
        else:
            print(i,'不及格')
判断及格(55,66,77,88,99,100)'''









#homework
def jisuan2(a):
    b=15
    c=(a-3)*2.3
    d=(a-15)*3.45
    f=c+d+b
    print(f)
def jisuan(a):
    b=15
    if a<15 or a==15:
        c=(a-3)*2.3
        e=b+c
        print(e)
    else:
        jisuan2(a)
a=int(input('（整数）公里数'))
print(a)
if a<3 or a==3:
    print('13元')
else:
    jisuan(a)
    
#用了两个函数
        







'''def 汉堡(胚子,*小料):
        print('你要的胚子为:',胚子)
        print('汉堡的配料有:')
        for i in 小料:
            print('----',i)
        
汉堡('芝麻','生菜','cheers')'''
        
    
    
    