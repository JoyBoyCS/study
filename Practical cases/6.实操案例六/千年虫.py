lst1=[82,88,98,86,92,0,99]
lst2=[]
for i in lst1:
    if i ==0:
        a='200'+str(i)
    else:
        a='19'+str(i)
    lst2.append(int(a))
lst2.sort()
print(lst2)