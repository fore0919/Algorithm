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
