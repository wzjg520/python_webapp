__author__ = 'John Wang'

# 插入算法排序

def insertionSort(list):
    length = len(list)
    j = 1
    while j < length:
        key = list[j]
        i = j - 1
        while i >= 0 and list[i] > key:
            list[i+1] = list[i]
            i = i - 1
        list[i+1] = key
        j = j + 1;
    return list

list = insertionSort([6,2,3,2,78,23,3,2,3,4,2,3,2,1,4,67,9])
print(list)

