def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums

    mid = n // 2

    left_nums = merge_sort(nums[:mid])

    right_nums = merge_sort(nums[mid:])

    i, j = 0, 0

    res = []

    while i < len(left_nums) and j < len(right_nums):
        if left_nums[i] <= right_nums[j]:
            res.append(left_nums[i])
            i += 1
        else:
            res.append(right_nums[j])
            j += 1

    res += left_nums[i:]
    res += right_nums[j:]
    return res


if __name__ == "__main__":
    a = [3, 2, 1, 1, 1, 5, 6, 2, 3, 5, 2, 1, 8, 7, 1]
    b = merge_sort(a)
    print(b)
