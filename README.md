# 🧠 Backtracking Practice in Python

Welcome to my **Backtracking Practice** repository! This repo contains Python solutions to classic backtracking problems, often asked in coding interviews and competitive programming.

## 📚 What is Backtracking?

Backtracking is a recursive algorithmic technique used for solving problems that involve **decision trees**, such as generating combinations, permutations, or solving constraint-based puzzles. It works by:

1. **Making choices** from available options
2. **Recursively exploring** the consequences of each choice
3. **Undoing choices** (backtracking) when they lead to invalid solutions
4. **Finding all solutions** or the optimal solution

---

## 📁 Repository Structure

Each Python file in this repo represents a self-contained backtracking problem:

| Filename | Description | Difficulty | LeetCode |
|----------|-------------|------------|----------|
| `combination.py` | Find all combinations of numbers that sum to a target (numbers may be reused) | Medium | [LC #39](https://leetcode.com/problems/combination-sum/) |
| `letterCombinations.py` | Generate all letter combinations from a digit string using phone keypad mapping | Medium | [LC #17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |
| `nQueens.py` | Classic N-Queens problem – place N queens on an N×N board safely | Hard | [LC #51](https://leetcode.com/problems/n-queens/) |
| `permutatons.py` | Generate all possible permutations of a collection | Medium | [LC #46](https://leetcode.com/problems/permutations/) |
| `subset.py` | Generate all possible subsets (power set) of a set | Medium | [LC #78](https://leetcode.com/problems/subsets/) |
| `subset2.py` | Generate all unique subsets from a collection with duplicates | Medium | [LC #90](https://leetcode.com/problems/subsets-ii/) |
| `wordSearch.py` | Find if a word exists in a 2D board of characters | Medium | [LC #79](https://leetcode.com/problems/word-search/) |
| `ratMaze.py` | Find all paths for a rat to reach destination in a maze | Medium | Classic Problem |
| `knightConfigurations.py` | Validate knight's tour on a chessboard | Medium | [LC #2596](https://leetcode.com/problems/check-knight-tour-configuration/) |

---

## 🛠️ Getting Started

### Prerequisites

- Python 3.6 or higher
- Basic understanding of recursion and algorithms

### 1. Clone the Repository

First, clone the repository to your local machine using:

```bash
git clone https://github.com/hureramujeeb60/BackTracking-Practice.git
cd backtracking-practice
```

### 2. Run Individual Solutions

Each file can be run independently. For example:

```bash
python combination.py
python nQueens.py
python wordSearch.py
```

### 3. Run All Solutions

You can run all solutions at once using the main script:

```bash
python main.py
```

---

## 🎯 Problem Descriptions

### 1. **Combination Sum** (`combination.py`)
Given an array of distinct integers and a target, find all unique combinations where the chosen numbers sum to target. The same number may be chosen unlimited times.

**Example:**
```python
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
```

### 2. **Letter Combinations** (`letterCombinations.py`)
Given a string containing digits from 2-9, return all possible letter combinations that the number could represent (like on a phone keypad).

**Example:**
```python
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### 3. **N-Queens** (`nQueens.py`)
Place N chess queens on an N×N board so that no two queens attack each other.

**Example:**
```python
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
```

### 4. **Permutations** (`permutatons.py`)
Generate all possible permutations of a given list of numbers.

**Example:**
```python
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```

### 5. **Subsets** (`subset.py`)
Generate all possible subsets (the power set) of a given set of distinct integers.

**Example:**
```python
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
```

### 6. **Word Search** (`wordSearch.py`)
Given a 2D board and a word, find if the word exists in the grid.

**Example:**
```python
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: True
```

### 7. **Rat in a Maze** (`ratMaze.py`)
Find all possible paths for a rat to travel from top-left to bottom-right in a maze.

**Example:**
```python
Input: maze = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
Output: ["DDRDRR","DRDDRR"]
```

### 8. **Knight's Tour Validation** (`knightConfigurations.py`)
Check if a given configuration represents a valid knight's tour on a chessboard.

---

## 📈 Complexity Analysis

| Problem | Time Complexity | Space Complexity |
|---------|----------------|------------------|
| Combination Sum | O(N^(T/M)) | O(T/M) |
| Letter Combinations | O(4^N × N) | O(N) |
| N-Queens | O(N!) | O(N²) |
| Permutations | O(N! × N) | O(N) |
| Subsets | O(2^N × N) | O(N) |
| Word Search | O(N × M × 4^L) | O(L) |
| Rat in a Maze | O(2^(N²)) | O(N²) |
| Knight's Tour | O(8^(N²)) | O(N²) |

*Where N = array/board size, M = minimum candidate value, T = target value, L = word length*

---

## 🔑 Key Backtracking Patterns

### 1. **Basic Template**
```python
def backtrack(path, choices):
    if is_solution(path):
        solutions.append(path[:])
        return
    
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, remaining_choices)
            path.pop()  # Undo the choice
```

### 2. **Common Techniques**
- **Pruning**: Skip branches that cannot lead to valid solutions
- **State restoration**: Undo changes after exploring a branch
- **Memoization**: Cache results for overlapping subproblems
- **Early termination**: Stop when a solution is found (if only one is needed)

---

## 🧪 Testing

Each solution includes a `__main__` block with test cases. To add your own tests:

```python
if __name__ == "__main__":
    # Add your test cases here
    test_input = [...]
    solution = Solution()
    result = solution.method_name(test_input)
    print(f"Input: {test_input}")
    print(f"Output: {result}")
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to add more backtracking problems or improve existing solutions:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/new-problem`)
3. Commit your changes (`git commit -m 'Add new backtracking problem'`)
4. Push to the branch (`git push origin feature/new-problem`)
5. Open a Pull Request

### Contribution Guidelines
- Follow PEP 8 style guide
- Include problem description and examples
- Add time/space complexity analysis
- Include test cases in the `__main__` block

---

## 📚 Resources

- [LeetCode Backtracking Problems](https://leetcode.com/tag/backtracking/)
- [GeeksforGeeks - Backtracking Algorithms](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Backtracking Algorithm Visualization](https://algorithm-visualizer.org/backtracking)
- [MIT OCW - Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)

---

## 👤 Author

**Hurera Mujeeb**

- GitHub: [@hureramujeeb60](https://github.com/hureramujeeb60)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/hurera-mujeeb-b88791235/)

---

⭐ If you found this repository helpful, please give it a star!
