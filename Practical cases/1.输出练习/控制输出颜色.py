'''
样式：
0: 无样式
1: 加粗（高亮度）
2: 低亮度
3: 斜体
4: 下划线
5: 慢闪烁
6: 快闪烁
7: 反显
8: 隐藏
9: 删除线

前景色：
30: 黑色
31: 红色
32: 绿色
33: 黄色
34: 蓝色
35: 紫色
36: 青色
37: 白色

背景色：
40: 黑色
41: 红色
42: 绿色
43: 黄色
44: 蓝色
45: 紫色
46: 青色
47: 白色
所有的这些代码都需要放置在方括号（[ 和 ]）中，并以 \033 开头，以 m 结尾。例如，\033[1;33;44m 表示加粗的文字，黄色前景和蓝色背景。
'''

print('\033[0;35m     图书音像勋章                      ')
print('\033[35m------------------------------------------')