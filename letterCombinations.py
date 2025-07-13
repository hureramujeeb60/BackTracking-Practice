from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        res = []
        
        def backtrack(i, res, curStr):
            if i == len(digits):
                res.append(curStr)
                return
        
            digitLetters = dict[digits[i]]
            for letter in digitLetters:
                backtrack(i+1, res, curStr + letter)

        if digits:
            backtrack(0, res, "")
        
        return res
    
if __name__ == "__main__":
    digits = "23"
    sol = Solution()
    print(sol.letterCombinations(digits))