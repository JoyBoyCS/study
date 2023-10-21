a=[]
b=[]
for i in range(0,5):
    x=input('请输入商品，每次只能输入一件：')
    a.append(x)
    
for item in a:
    print(item)
    


for item1 in a:
    y=input('请输入要购买商品的编号：')
    if y in item1:
        b.append(item1)
        print('商品已经添加到购物车，请继续输入')
    elif y=='q':
        print('您购物车的商品为：')
        for item2 in b:
            print(item2)
        break
 