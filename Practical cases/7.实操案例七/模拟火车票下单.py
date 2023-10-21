print('车次  ','出发站-到达站  ','出发时间  ','到达时间  ','历时')
print('G1569 ','北京南-天津南  ','18：05    ','18:39     ','00:34')
print('G1567 ','北京南-天津南  ','18：15    ','18:49     ','00:34')
print('G8917 ','北京南-天津西  ','18：20    ','19:19     ','00:59')
print('G203  ','北京南-天津南  ','18：35    ','19:09     ','00:34')

lst1 = ['G1569 ','北京南-天津南  ','18：05    ','18:39     ','00:34']
lst2 = ['G1567 ','北京南-天津南  ','18：15    ','18:49     ','00:34']
lst3 = ['G8917 ','北京南-天津西  ','18：20    ','19:19     ','00:59']
lst4 = ['G203  ','北京南-天津南  ','18：35    ','19:09     ','00:34']

lst5 = [lst1,lst2,lst3,lst4]
lst6=[lst1[0].strip(),lst2[0].strip(),lst3[0].strip(),lst4[0].strip()]
a = input('请输入要购买的车次：')
if a not in lst6:
    print('没有找到对应的车次。')
else:
    b = input('请输入乘车人，如果是多人，请使用逗号分隔：')
    for i, lst in enumerate(lst5):
        if a.strip() == lst[0].strip():  # 使用 strip() 函数移除字符串的首尾空格
            print(f'您已经购买了{lst[0].strip()}次列车，{lst[1].strip()} {lst[2].strip()}开，请{b}尽快换取纸制车票。')
            break
   