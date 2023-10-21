coffee = ('1.蓝山','2.卡布奇诺','3.拿铁','4.皇家咖啡','5.女王咖啡','6.美丽与哀愁')

print('您好！欢迎逛了小喵咖啡屋')
print('本店经营的咖啡有：')
while True:
    flag=False
    num = input(' '.join(coffee) + ' 请输入您喜欢的咖啡编号：')
    for item in coffee:
        if num in item:   
            print(f'您的咖啡{item[2::]}到了，请您慢用')
            flag=True
            break
    if not flag:
        print('您输入的编号错误，请重新输入!')
    else:
        break