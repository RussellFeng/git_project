def binary_search(alist, item):
    # 递归调用

    n = len(alist)
    
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False

def binary_search_2(alist, item):
    #非递归调用
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return False





if __name__ == "__main__":
    a = [1,2,3,4,5,6]
    print(binary_search(a, 5))
    print(binary_search(a, 11))
    print(binary_search_2(a, 5))
    print(binary_search_2(a, 11))
    print(binary_search_2(a, 3))