def find_answer(question):
    with open('D:/Code/python/Practical cases/15.实操案例十五/replay.txt','r',encoding='gbk') as file:
        while True:
            line=file.readline()
            if not line:    #if line==''到文件末尾结束
                break
            #字符串的分割
            keyword=line.split('|')[0]
            replay=line.split('|')[1]
            if keyword in question:
                return replay
    return False

if __name__ == '__main__':
    question=input('您好，请问您有什么问题呢？')
    while True:
        if question=='bye':
            break
        #开始在文件中查找
        replay=find_answer(question)
        if not replay:  #如果回复的是false， not false==true
            question=input('我不知道你在说什么，您可以问一些关于订单，物流，账户，支付的问题（退出请输入bye）')
        else:
            print(replay)
            question=input('您可以继续问一下关于订单，物流，账户，支付的问题（退出请输入bye）')
    print('再见')