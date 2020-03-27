"""快速排序的实现
"""


def quick_sort(alist, first=0, last=None):
    """快速排序"""
    if last is None:
        last = len(alist) - 1   # 设置末尾项的序号
    if first >= last:           # 开头项序号大于等于末尾项则返回
        return
    mid_val = alist[first]      # 中间值mid_val设为开头项的值
    low = first                 # 低端序号low指向开头项
    high = last                 # 高端序号hight指向末尾项
    while low < high:           # low小于high时执行一轮操作
        while low < high and alist[high] >= mid_val:
            high -= 1
        alist[low] = alist[high]
        while high > low and alist[low] < mid_val:
            low += 1
        alist[high] = alist[low]
    alist[low] = mid_val        # low和high重叠时将所指项赋值为mid_val
    quick_sort(alist, first, low - 1)
    quick_sort(alist, low + 1, last)


if __name__ == "__main__":
    alist = [23, 54, 12, 8, 48, 16, 88, 3, 56]
    print(alist)
    quick_sort(alist)
    print(alist)
