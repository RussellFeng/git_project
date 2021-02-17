def insert_sort(nums):
    '''
    插入排序
    '''
    n = len(nums)
    for i in range(n):
        j = i
        while j > 0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
            
        
    
    
    
if __name__ == '__main__':
    a = [3,2,1,8,2,5,2]
    insert_sort(a)
    print(a)