from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.solve(candidates,0, [], res, target)
        return res

    def solve(self, nums, index, path, res, target):
        if target == 0:
            res.append(path[:])
            return
        
        if target < 0:
            return
        
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.solve(nums, i, path, res, target-nums[i])
            path.pop()

if __name__ == "__main__":
    nums = [2,3,6,7]
    target = 7
    sol = Solution()
    res = sol.combinationSum(nums, target)
    print(res)