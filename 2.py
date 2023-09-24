def zhuan(n):
    if n==1:
        ruturn ''1''
    else:
        yushu=n%2
        return zhuan(n//2)+str(yushu)
print()