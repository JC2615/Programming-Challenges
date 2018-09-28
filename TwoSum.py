def twoSum(nums, target):
    add = 0
    curr = 0
    index = 0
    index2 = 0
    for i in nums:
        curr = i
        index = nums.index(curr)
        for otheri in range(index + 1, len(nums)):
            add = nums[otheri] + curr
            index2 = nums.index(nums[otheri], index + 1)
            if add == target:
                indeces = [index, index2]
                return indeces
        
array = [3,3]    
print(twoSum(array, 6))