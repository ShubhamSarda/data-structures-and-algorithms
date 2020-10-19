class Solution:
    def twoSum(self, nums, target):               
        store = {}

        for i in range(len(nums)):            
            if nums[i] in store:
                return [store[nums[i]], i]
            else:
                store[target-nums[i]] = i


## Example Execution ##
obj = Solution()
result = obj.twoSum([2,7,11,15], 9)
print(result)