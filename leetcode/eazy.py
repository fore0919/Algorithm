from collections import Counter
from typing import List


class Solution:
    """
    88. Merge Sorted Array
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx = 0
        for i in range(len(nums1)):
            if i >= m and idx <= n and nums1[i] == 0:
                nums1[i] = nums2[idx]
                idx += 1
        nums1.sort()

    """
    27. Remove Element
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        while len(nums) > k:
            num = nums.pop(0)
            if num != val:
                nums.append(num)
        return k

    """
    26. Remove Duplicates from Sorted Array
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt

    """
    169. Majority Element
    """

    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common(1)[0][0]
        # return sorted(nums, key=lambda x : - nums.count(x))[0]

    """
    121. Best Time to Buy and Sell Stock
    """

    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            sell = max(sell, prices[i] - buy)
        return sell
