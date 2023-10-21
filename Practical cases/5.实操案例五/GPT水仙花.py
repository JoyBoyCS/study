#方法1：常规硬算
for i in range(100,1000):
    ones=i%10
    tens=(i//10)%10
    hundreds=i//100
    if (ones**3 + tens**3 + hundreds**3)==i:
        print(i)
print('-------------------------------------------')

#方法2：GPT上的方法
for num in range(100, 1000):
    count = [int(i) for i in str(num)]  # 将数字转换为字符列表

    if sum(d**3 for d in count) == num:
        print(num)
print('--------------------------------------')

#方法3：根据GPT上案例改进
for num in range(100, 1000):
    if sum(int(d)**3 for d in str(num)) == num:
        print(num)