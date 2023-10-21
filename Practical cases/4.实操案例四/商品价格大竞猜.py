
attempt=5
while attenmpt>0:
    try:
        print('今日竞猜商品为小米扫地机器人：价格在[1000-1500之间]')
        print('------------------------------------------------')
        price=int(input('请输入您的竞猜价格：'))
        if price==1400:
            print('\033[1;32m恭喜您猜对了！成功获得小米扫地机器人！\033[m')
            break
        elif price<1400 and price>=1000:
            print('\033[1;33m很遗憾价格偏低了\033[m')
            attenmpt=attenmpt-1
            print(f'您还剩余\033[1;36m{attenmpt}\033[m次机会，请加油！')
        elif price>1400 and price<=1500:
            print('\033[1;33m很遗憾价格偏高了\033[m')
            attenmpt=attenmpt-1
            print(f'您还剩余\033[1;36m{attenmpt}\033[m次机会，请加油！')
        else:
            print('\033[1;35m您输入的价格不在竞猜范围内！\033[m\033[1;32m（不会扣除剩余机会呦~）\033[m')   
    except:
        print('\033[1;35m您的输入错误！请输入数字！\033[m\033[1;32m（不会扣除剩余机会呦~）\033[m') 
if attempt==0:
    print('\033[1;31m对不起，您的竞猜次数已用完\033[m')