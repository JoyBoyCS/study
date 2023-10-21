#方法1 
import string
lst=list(string.ascii_lowercase)
for letter in lst:
    print(f'字母{letter}的ASCII码值为{ord(letter)}')    #ord()获取字符的ASCII值
    
print('------------------------------------------------------')
#方法2
x=97    #代表的是a的ASCII值
for i in range(1,27):
    print(chr(x),'--->',x)
    x+=1
    
print('------------------------------------------------------')
#方法3
x=97
while x <123:
    print(chr(x),'----->',x)
    x+=1

'''
string是Python的一个标准库，提供了许多常用字符串的常量和工具函数。

以下是string模块中一些常见的属性：

string.ascii_letters：包含所有的英文大写和小写字母，即’abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ’
string.ascii_lowercase：包含所有英文小写字母，即’abcdefghijklmnopqrstuvwxyz’
string.ascii_uppercase：包含所有英文大写字母，即’ABCDEFGHIJKLMNOPQRSTUVWXYZ’
string.digits：所有十进制数字，即’0123456789’
string.hexdigits：所有十六进制数字，即’0123456789abcdefABCDEF’
string.octdigits：所有八进制数字，即’01234567’
string.punctuation：所有标点符号
string.printable：所有可打印的ASCII字符
string.whitespace：所有的空白字符，包括空格、换行(\n)、制表符(\t)等。
此外，string模块还提供了一些用于处理字符串的类和方法，比如string.Formatter类用于字符串的格式化操作，string.Template类提供了另一种方式在新字符串中替换部分内容。
'''