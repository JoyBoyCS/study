def fun():
    print('二进制转换'.center(50,'-'))
    num=int(input('请输入一个十进制整数：'))    #将str类型转换成int类型
    print(num,'的二进制数为：',bin(num))    #第一种写法，使用了个数可变的位置参数
    print(str(num)+'的二进制数为：'+bin(num))   #第二种写法，使用了"+"作为连接符（+的左右均为str类型才行）
    print('%s的二进制数为：%s' % (num,bin(num)))    #第三种写法，格式化字符串
    print('{0}的二进制数为：{1}'.format(num,bin(num)))  #第三种写法，格式化字符串
    print(f'{num}的二进制数为：{bin(num)}') #第三种写法，格式化字符串

    print('八进制转换'.ljust(50,'-'))
    print(f'{num}的八进制数为：{oct(num)}') 

    print('十六进制转换'.rjust(50,'-'))
    print(f'{num}的十六进制数为：{hex(num)}') 

if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('输入错误！只能输入整数')
        