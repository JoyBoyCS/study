
attempt =0

while attempt<3:
    pwd=input('支付宝支付密码：')
    if pwd.isdigit():

        if pwd=='8888':
            print('密码正确！支付成功！')
            break
        else:
            print('密码不正确！支付失败！')
            attempt+=1
    else:
        print('支付数据不合法')
if attempt==3:
    print('达到最大尝试次数，请明天再试')
