
attempt=3
while attempt>0:
    uname=input('请输入用户名：')
    pwd=input('请输入密码：')

    if uname=='admin' and pwd=='w123456':
        print('登录成功！')
        break
    else:
        print('账号或密码错误，请重新输入')
        attempt-=1
        print(f'您还有{attempt}次机会！！')
if attempt==0:
    print('对比起，三次输入均有误，请联系管理员')    
    
    