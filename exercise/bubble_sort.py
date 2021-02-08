def bubble_sort(nums):
    '''
    冒泡排序
    '''
    n = len(nums)
    for i in range(n):
        flag = 0
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = 1
            if flag == 0:
                return

if __name__ == "__main__":
    nums = [3, 1, 2, 9, 6]
    bubble_sort(nums)
    print(nums)
    