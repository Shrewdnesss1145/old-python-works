def hws(s):
    if len(s)<=2:
        if s[0]==s[-1]:
            return 'yes'
        else:
            return 'no'
    else:
        if s[0]==s[-1]:
            return hws(s[1:-1])
        else:
            return 'not hws'
a=input('输入一个字符串')
print(hws(a))