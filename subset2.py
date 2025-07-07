from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.solve(nums,0,[],res)
        return res
    
    def solve(self, nums,index,path,res):
        res.append(path[:])
        
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            
            path.append(nums[i])
            self.solve(nums, i+1, path, res)
            path.pop()

if __name__ == "__main__":
    nums=[1,2,2]
    sol = Solution()
    result = sol.subsetsWithDup(nums)
    print(result)