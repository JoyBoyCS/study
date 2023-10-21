
import prettytable as pt 

#显示座席
def show_ticket(row_num):
    tb=pt.PrettyTable() #创建了一个 PrettyTable 对象，然后将其存储在变量 tb 中
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5'] #field_names是PrettyTable对象的一个属性，用于设置或获取表格的列标题
    for i in range(row_num):
        lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
        tb.add_row(lst) #tb.add_row(lst) 是 prettytable 库中 PrettyTable 类的一个方法。它用于向 PrettyTable 对象（在这里是 tb）添加一行数据
    print(tb)
    
#订票
def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        if int(row)==i+1:
            lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
            lst[int(column)]='\033[31m已售\033[m'
            tb.add_row(lst)
        else:
            lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
            tb.add_row(lst)
    print(tb)
    
if __name__ == '__main__':
    row_num=13
    show_ticket(row_num)
    choose_num=input('请输入选择的座位编号：')
    try:
        row,column=choose_num.split(',')
    except:
        print('输入格式有误，比如13排5号座位，应输入13,5')
    order_ticket(row_num,row,column)
    