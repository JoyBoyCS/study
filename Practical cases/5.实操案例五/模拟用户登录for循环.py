for i in range(1,4):
    user_name=input('请输入用户名：')
    user_pwd=input('请输入密码：')
    if user_name=='admin' and user_pwd=='8888':
        print('登录成功')
        break
    else:
        print('账号或密码错误，请重新输入')
        if i <3:
            print(f'您还有{3-i}次机会！！！')
else:       
    print('对比起，三次输入均有误，请联系管理员')    
        
    
