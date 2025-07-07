from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.solve(nums, 0, [], res)
        return res

    def solve(self,nums, index, path, res):
        res.append(path[:])
        
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.solve(nums, i+1, path, res)
            path.pop()
                
if __name__ == "__main__":
    nums=[1,2,3]
    sol = Solution()
    result = sol.subsets(nums)
    print(result)