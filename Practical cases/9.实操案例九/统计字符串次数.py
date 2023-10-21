s='hellopython,Hellojava,hellojango'

x=0
a=input('请输入要统计的字符：')
for i in s:
    if a==i:
        x+=1
print(x)