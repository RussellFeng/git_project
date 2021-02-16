def quick_sort(nums, left, right):
    if left >= right:
        return
    mid_value = nums[left]
    i = left
    j = right
    while i < j:
        while i < j and nums[j] >=  mid_value:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <  mid_value:
            i += 1
        nums[j] = nums[i]
    nums[j] = mid_value
    quick_sort(nums, left, i)
    quick_sort(nums, i+1, right)


if __name__ == "__main__":
    a = [1,5,2,3,5,6,2,1]
    quick_sort(a, 0, len(a)-1)
    print(a)