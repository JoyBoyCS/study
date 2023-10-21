'''
在Python编程中，random是一个内置模块，可以用来生成伪随机数。这个模块包含多种函数，例如：

random.random()：返回一个[0.0, 1.0)之间的随机浮点数
random.randint(a, b)：返回一个[a, b]之间的随机整数
random.choice(seq)：从序列seq中随机选择一个元素
random.shuffle(lst)：将列表lst中的元素随机打乱
'''
import random
price=random.randint(1000,1500)
print('今日竞猜商品为小米扫地机器人：价格在[1000-1500之间]:')
guess=int(input())
if guess>price:
    print('大了')
elif guess<price:
    print('小了')
else:
    print('猜对了')
print('真实价格为：',price)