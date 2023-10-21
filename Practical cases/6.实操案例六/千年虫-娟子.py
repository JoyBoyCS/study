year=[82,88,98,86,92,0,99]
print('原列表：',year)
for index,value in enumerate(year):     #numerate() 是 Python 的内置函数，它接收一个可迭代的对象（如列表、元组或字符串）作为参数，并返回一个枚举对象。这个枚举对象产生由两个部分组成的元组：一个是元素的索引，另一个是可迭代对象的元素本身
    #print(index,value)
    if str(value)!='0':
        year[index]=int('19'+str(value))
    else:
        year[index]=int('200'+str(value))
print('修改后的列表：',year)
#列表排序
year.sort()
print('排序之后的列表为：',year)