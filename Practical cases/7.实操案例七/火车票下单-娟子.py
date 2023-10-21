
trains = {
    'G1569': ['北京南-天津南', '18：05', '18:39', '00:34'],
    'G1567': ['北京南-天津南', '18：15', '18:49', '00:34'],
    'G8917': ['北京南-天津西', '18：20', '19:19', '00:59'],
    'G203': ['北京南-天津南', '18：35', '19:09', '00:34']
}
print('车次  ','出发站-到达站  ','出发时间  ','到达时间  ','历时')
for item in trains:
    print(item,end=' ')
    for i in trains[item]:
        print(i,end=' ')
    print() #换行
train_no = input('请输入要购买的车次：')
persons=input('请输入乘车人，如果是多人，请使用逗号分隔：') 
s=f'您已经购买了{train_no}次列车'
s_info=trains[train_no] #获取车次详情信息
s+=s_info[0]+''+s_info[1]+'开'
print(f'{s}请{persons}尽快取走车票')