# 冒泡排序
def bubble_sort(l):
    for j in range(len(l)):
        for i in range(len(l) - 1 - j):
            if l[i] > l[i + 1]:
                l[i + 1], l[i] = l[i], l[i + 1]

    return l


# 插入排序
def insert_sort(l):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]


# 选择排序
def select_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]


# 归并排序
def merge(l, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if l[i] <= l[j]:
            tmp.append(l[i])
            i += 1
        else:
            tmp.append(l[j])
            j += 1
    while i <= mid:
        tmp.append(l[i])
        i += 1
    while j <= high:
        tmp.append(l[j])
        j += 1
    l[low:high + 1] = tmp


def merge_sort(l, low, high):
    if low < high:
        mid = (high + low) // 2
        merge_sort(l, low, mid)
        merge_sort(l, mid + 1, high)
        merge(l, low, mid, high)


# 快速排序
def partition(l, low, high):
    p = l[high]
    i = low
    for j in range(low, high):
        if l[j] < p:
            l[i], l[j] = l[j], l[i]
            i += 1
    l[i], l[high] = l[high], l[i]
    return i


def quick_sort(l, low, high):
    if low < high:
        mid = partition(l, low, high)
        quick_sort(l, low, mid - 1)
        quick_sort(l, mid + 1, high)


l = [7, 4, 11, 20, 8, 2, 9]
# bubble_sort(l)
# insert_sort(l)
# select_sort(l)
# merge_sort(l, 0, len(l) - 1)
quick_sort(l, 0, len(l)-1)
print(l)
