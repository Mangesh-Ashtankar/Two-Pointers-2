class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        count = 1
        j =1
        
        for i in range(1,len(nums)):
            # if same, update count
            if nums[i] == nums[i+1]:
                count = count+1
            
            # count reset
            else:
                count = 1
                
            # count <= 2
            if count <= 2:
                nums[j] = nums[i]
                j += 1
            
        return j
