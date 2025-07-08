from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, 0, result)
        return result
    
    def solve(self, nums,index, result):
        if index == len(nums):
            result.append(nums[:])
            return
        
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.solve(nums, index+1, result)
            nums[i], nums[index] = nums[index], nums[i]
            

if __name__ == "__main__":
    nums=[1,2,3]
    sol = Solution()
    result = sol.permute(nums)
    print(result)