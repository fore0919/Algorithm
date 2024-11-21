from collections import Counter
from typing import List


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
