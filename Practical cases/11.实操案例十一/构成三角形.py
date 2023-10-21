
def triangle(a,b,c):
    if (a+b)>c and (a+c)>b and (c+b)>a:
        return True
    else:
        return False
if __name__ == '__main__':
    flag=True
    while flag:
        try:
            a=int(input('请输入第一条边：'))
            b=int(input('请输入第二条边：'))
            c=int(input('请输入第三条边：'))
            if a<0 or b<0 or c<0:
                print('三条边不能是负数')
                flag=False
            elif triangle(a,b,c):
                print(f'a={a},b={b},c={c}能构成三角形')
                flag=False
            else:
                print(f'a={a},b={b},c={c}不能构成三角形')
                flag=False
        except:
            print('输入的类型错误，要求输出为整数，请重新输入!')
        