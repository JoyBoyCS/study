lst=[['01','01','01',22],
     ['02','02','02',11],
     ['03','03','03',33]]


for item in lst:
    item[0]='0000'+item[0]
    item[3]='${:.2f}'.format(item[3])
for item in lst:
    for i in item:
        print(i,end='  ')
    print()