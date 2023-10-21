
import random
def guess(num,guess_num):
    if num==guess_num:
        return 0
    if num<guess_num:
        return 1
    else:
        return -1
    
num=random.randint(1,100)    
for i in range(10):
    guess_num=int(input('输入一个1-100之间的数：'))
    result=guess(num,guess_num)
    if result==0:
        print('猜对了')
        break
    elif result==1:
        print('大了')
    elif result==-1:
        print('小了')
else:
    print('您真是一个大聪明！十次都没猜对')