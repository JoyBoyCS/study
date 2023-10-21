def Merge(a,start,mid,end):
    tmp = []  # 创建一个临时列表存储排序后的元素
    l = start  # 左边部分的起始索引
    r = mid+1  # 右边部分的起始索引

    # 当左右两部分都还有元素未处理时
    while l <= mid and r<= end:
        # 如果左边的元素小于或等于右边的元素
        if a[l] <= a[r]:
            tmp.append(a[l])  # 将左边的元素添加到临时列表
            l += 1  # 左边部分的当前索引加一
        else:
            tmp.append(a[r])  # 否则将右边的元素添加到临时列表
            r += 1  # 右边部分的当前索引加一

    # 如果左半部分还有剩余元素，就全部加到临时列表后面
    tmp.extend(a[l:mid+1])

    # 如果右半部分还有剩余元素，就全部加到临时列表后面
    tmp.extend(a[r:end+1])

    # 将排序后的元素复制回原数组
    for i in range(start,end+1):
        a[i] = tmp[i-start]

    print(a)  # 输出每次合并后的数组状态
    
def MergeSort(a,start,end):
    # 如果只有一个元素，就不需要再分解了，直接返回
    if start == end:
        return

    # 分解数组，计算中间位置的索引
    mid = (start + end) // 2

    # 对左半部分进行归并排序
    MergeSort(a, start, mid)

    # 对右半部分进行归并排序
    MergeSort(a, mid+1, end)

    # 合并两个已排序的子数组
    Merge(a, start, mid, end)

# 初始化一个无序的数组 'a'
a = [8, 5, 6, 4, 3, 7, 10, 2]

# 调用归并排序函数对数组 'a' 进行排序
MergeSort(a, 0, len(a)-1)