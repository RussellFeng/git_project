def shell_sort(nums):
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j >= gap and nums[j] < nums[j-gap]:
                nums[j], nums[j-gap] = nums[j-gap], nums[j]
                j -= gap
        gap = gap // 2


if __name__ == "__main__":
    a = [3,1,2,6,1,2,3,5]
    shell_sort(a)
    print(a)