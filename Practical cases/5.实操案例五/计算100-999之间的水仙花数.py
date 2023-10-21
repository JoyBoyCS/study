#方法1
for i in range(100,1000):
    ones=i%10
    tens=(i//10)%10
    hundreds=i//100
    if (ones**3 + tens**3 + hundreds**3)==i:
        print(i)
print('-------------------------------------------')
