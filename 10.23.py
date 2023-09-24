'''c=input('添加的零食:')
a={
    '水果':'香蕉',
    '蔬菜':'西红柿',
    '海鲜':'螃蟹',
    '肉类':'猪肉'}'''
'''b=a.get('零食')
if b==None:
    a.update({'零食':c})
    print(a)'''


a=[]
dict={
    '语文':82,
    '数学':95,
    '英语':88,
    '编程':98,
    '音乐':80,
    '美术':59}
b=dict.items()
for i,j in b:
    if j<60 or j>90:
        print(i)

        


    