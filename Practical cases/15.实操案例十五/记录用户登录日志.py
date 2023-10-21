import time
def show_info():
    print('请输入提示数字，执行相应操作：0.退出 1.查看日志')

#记录日志
def write_logininfo(username):
    with open('D:/Code/python/Practical cases/15.实操案例十五/log.txt','a',encoding='utf-8') as file:
        s=f'用户名{username},登录时间：{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')
   
   
#读取日志
def read_loginifo():
    with open('D:/Code/python/Practical cases/15.实操案例十五/log.txt','r',encoding='utf-8') as file:
        while True:
            line=file.readline()
            if line =='':
                break
            else:
                print(line,end='\t')
     
if __name__ == '__main__':
    username=input('请输入用户名：')
    pwd=input('请输入密码：')
    if 'admin'==username and '8888'== pwd:
        print('登录成功！！！')
        write_logininfo(username)   #记录日志
        show_info() #提示用户要执行什么操作
        num=int(input('输入操作数字：'))
        while True:
            if num==0:
                print('退出成功')
                break
            elif num==1:
                print('查看登录日志')
                read_loginifo() #读取日志
                num = int(input('请输入操作数字:'))
            else:
                print('您的输入有误！！')
                show_info()
                num = int(input('请输入操作数字：'))
    else:
        print('对不起用户名或者密码不正确')
    
    
    
    
    
    '''
    print(time.time())  #秒
    print(time.localtime(time.time()))
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
    '''