def select_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
        
    
    
if __name__ == "__main__":
    a = [1,2,1,5,3,2,1,7,5,3,8]
    select_sort(a)
    print(a)