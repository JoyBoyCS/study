coffee = ('蓝山','卡布奇诺','拿铁','皇家咖啡','女王咖啡','美丽与哀愁')

print('您好！欢迎逛了小喵咖啡屋')
print('本店经营的咖啡有：')
for index,item in enumerate(coffee):
    print(index+1,'.',item,end=' ')
    
index = int(input('\n请输入您喜欢的咖啡编号：'))
if 0<index<=len(coffee):
    print(f'您的咖啡{coffee[index-1]}好了，请您慢用')