import random

num=random.randint(1,100)
count=0
'''
while True:
    try:
        guess=int(input('我在心中有个1-100之间的数，请你猜一猜：'))
        count+=1
        if guess==num:
            print(f'恭喜你猜对了！\n您一共猜了{count}次\n还凑合')
            break
        elif guess<num:
            print('小了')
        elif guess>num:
            print('大了')
    except:
        print('输入错误！请输入1-100之间的数字')
'''
for i in range(1,99999):
    try:
        guess=int(input('我在心中有个1-100之间的数，请你猜一猜：'))
        if guess==num:
            print(f'恭喜你猜对了！\n您一共猜了{i}次')
            if i<7:
                print('真聪明！')
            elif i<=12:
                print('还凑合')
            else:
                print('卧槽你还真是个小天才！')
            break
        elif guess<num:
            print('小了')
        elif guess>num:
            print('大了')      
    except:
        print('输入错误！请输入1-100之间的数字')