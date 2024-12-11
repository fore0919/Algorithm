from collections import Counter, defaultdict, deque
from typing import List, Optional


class Solution:
    """
    80. Remove Duplicates from Sorted Array II
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.most_common():
            while v > 2:
                idx = nums.index(k)
                nums.pop(idx)
                v -= 1
        return sum(counter.values())

    def removeDuplicates2(self, nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k

    """
    189. Rotate Array
    """

    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    """
    122. Best Time to Buy and Sell Stock II
    """

    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if buy < prices[i]:
                sell += prices[i] - buy
            buy = prices[i]
        return sell

    """
    55. Jump Game
    """

    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        for num in nums:
            if distance < 0:
                return False
            if distance < num:
                distance = num
            distance -= 1
        return True

    """
    45. Jump Game II
    """

    def jump(self, nums: List[int]) -> int:
        answer, start, stop = 0, 0, 0
        while stop < len(nums) - 1:
            jump = 0
            for i in range(start, stop + 1):
                jump = max(jump, i + nums[i])
            start = stop + 1
            stop = jump
            answer += 1
        return answer

    """
    274. H-Index
    """

    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        return max(map(min, enumerate(citations, start=1)))

    """
    238. Product of Array Except Self
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1] * len(nums)
        left, right = 1, 1
        for i in range(len(nums)):
            arr[i] *= left
            left *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            arr[j] *= right
            right *= nums[j]
        return arr

    """
    134. Gas Station
    """

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(cost) - sum(gas)) > 0:
            return -1
        start = 0
        current = 0
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            if current < 0:
                current = 0
                start = i + 1
        return start

    """
    209. Minimum Size Subarray Sum
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_size = len(nums) + 1
        current_sum, cnt = 0, 0
        for idx, val in enumerate(nums):
            current_sum += val
            while current_sum >= target:
                window_size = min(window_size, idx - cnt + 1)
                current_sum -= nums[cnt]
                cnt += 1
        return 0 if window_size > len(nums) else window_size


import random


class RandomizedSet:
    """
    380. Insert Delete GetRandom O(1)
    """

    def __init__(self):
        self.arr = []
        self.dic = {}

    def hash_map(self, val):
        return val in self.dic

    def insert(self, val: int) -> bool:
        if self.hash_map(val):
            return False

        self.arr.append(val)
        self.dic[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if not self.hash_map(val):
            return False

        idx = self.dic[val]
        self.arr[idx] = self.arr[-1]
        self.dic[self.arr[-1]] = idx
        self.arr.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


class Solution2:
    """
    36. Valid Sudoku
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    """

    def isValidSudoku_set(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                box_idx = (i // 3, j // 3)
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in columns[j]
                    or board[i][j] in boxes[box_idx]
                ):
                    return False
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                boxes[box_idx].add(board[i][j])
        return True

    def isValidSudoku_bitmask(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        columns = [0] * 9
        boxes = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                x = ord(board[i][j]) - ord("1")
                mask = 1 << x
                box_idx = (i // 3) * 3 + (j // 3)
                if (
                    (rows[i] & mask)  # 비교하는 비트가 둘다 참이면 만족
                    or (columns[j] & mask)
                    or (boxes[box_idx] & mask)
                ):
                    return False
                rows[i] |= mask  # 비교하는 비트가 둘중에 하나라도 참이면 만족
                columns[j] |= mask
                boxes[box_idx] |= mask
        return True

    def isValidSudoku_eazy(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    res += [
                        (i, element),
                        (element, j),
                        (i // 3, j // 3, element),
                    ]
        return len(res) == len(set(res))

    """
    199. Binary Tree Right Side View
    """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution3:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if not root:
            return answer
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                current = q.popleft()
                if i == n - 1:
                    answer.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return answer
