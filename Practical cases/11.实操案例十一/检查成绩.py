try:
    score=int(input('请输入分数：'))
    if 0 <= score <= 100:
        print('分数为：',score) 
    else:
        print('请输入正确的分数')
except:
    print('输入错误')
