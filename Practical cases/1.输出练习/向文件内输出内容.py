'''1.使用print方式进行输出(输出目的地是文件)'''
fp= open('d:/code/test.txt','w')
print('sdasdasdas',file=fp)
fp.close()

'''2.使用文件的读写操作'''
with open('d:/code/test2.txt','w',encoding='utf-8') as a:
    print('11122314',file=a)