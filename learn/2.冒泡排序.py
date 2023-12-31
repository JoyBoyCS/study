def BubbleSort(a):
    n = len(a)  # 获取列表长度

    # 外层循环，从后往前遍历每一个元素（除了第一个）
    for i in range(n - 1, 0, -1):
        # 内层循环，从前往后遍历，直到外层循环当前处理的元素
        for j in range(i):
            # 如果当前元素大于下一个元素
            if a[j] > a[j + 1]:
                # 交换元素位置，使较大的元素向后移动
                a[j], a[j + 1] = a[j + 1], a[j]
        print(a)  # 打印每次排序后的列表状态

# 定义列表 'a'
a = [5,6,8,4,3,7,10,2]

# 调用冒泡排序函数对列表 'a' 进行排序
BubbleSort(a)