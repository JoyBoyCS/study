import os
# 输入商品信息，并存入文件
filename='D:/Code/python/Practical cases/6.实操案例六/goods.txt'
if not os.path.exists(filename):    #检查filename文件是否存在
    lst1=[]
    for i in range(0,5):
        goods=input('请输入商品，每次只能输入一件：')
        lst1.append(goods)

    with open(filename, 'w',encoding='utf-8') as f:
        for item in lst1:
            f.write(item + '\n')
            print(item)
else:   # 如果文件存在，从文件中读取商品信息
    with open(filename, 'r',encoding='utf-8') as f:
        lst1 = f.read().splitlines()

lst2=[]   
while True:
    num=input('请输入要购买商品的编号：')
    if num=='q':
        break   #退出while循环

    found = False  # 标志变量，表示是否找到匹配的商品
    for item in lst1:
        if item.find(num) != -1:  #find() 是Python中字符串的一个方法，用于检测字符串中是否包含子字符串。如果包含子字符串，则返回其开始的索引值；否则返回 -1
            found = True  # 找到匹配的商品，无论是否已经购买过
            if item not in lst2:  # 检查商品是否已经在 lst2 中
                lst2.insert(0, item)  # 将商品插入到 lst2 的开始位置
            else:
                print('您已经购买过这个商品了！')
            break   #退出for循环
    
    if not found:  # 如果所有商品都被检查过，没有找到匹配项，则提示错误
        print('输入错误！请输入正确的编号')

print('您购物车的商品为：')
for i in lst2:
    print(i)
    
    
    
   
