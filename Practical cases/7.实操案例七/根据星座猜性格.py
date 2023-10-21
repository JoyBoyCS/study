zodiac=['白羊座','金牛座','双子座','巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座','摩羯座','水瓶座','双鱼座']
character=['热情冲动','稳重实际','善变聪明','敏感细心','自信热情',' 细致勤奋','和平公正','强烈执着','自由乐观','踏实稳定','独立创新','梦幻敏感']
dictionary=dict(zip(zodiac,character))

flag=True
while flag:
    a=input('请您输入您的星座名称：')
    if a in dictionary:
        b=dictionary.get(a)
        print(f'{a}的性格特点是：{b}')
        while True:
            choice=input('请问您是否还要继续查询呢？继续查询请输入y，退出查询请输入n：')
            if choice=='y':
                break
            
            elif choice=='n':
                flag=False
                break
            else:
                print('您的输入错误，请重新输入！')
    else:
        print('您的输入错误！请输入正确的星座名称')