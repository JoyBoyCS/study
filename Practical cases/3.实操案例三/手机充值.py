def fun():
    print('用户手机账户原有话费金额为：\033[0;35m8元\033[m')
    money=int(input('请输入充值金额：'))
    money+=8
    print('当前余额为：\033[0;32m',money,'元\033[m')
    
if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('您的输入有误，只能充值整数金额')