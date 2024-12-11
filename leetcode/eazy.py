from collections import Counter, deque
from typing import List, Optional


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

    """
    125. Valid Palindrome
    """

    def isPalindrome(self, s: str) -> bool:
        string = ""
        for x in s:
            if x.isalpha():
                string += x.lower()
            elif x.isdigit():
                string += x
        n = len(string)
        if string[: (n // 2) + (n % 2)] == "".join(reversed(string[n // 2 :])):
            return True
        return False

    """
    383. Ransom Note
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in list(set(ransomNote)):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

    """
    228. Summary Ranges
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if not nums:
            return answer
        start = nums[0]
        for i in range(1, len(nums) + 1):
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    answer.append(str(start))
                else:
                    answer.append(f"{start}->{nums[i - 1]}")
                if i < len(nums):
                    start = nums[i]
        return answer

    """
    20. Valid Parentheses
    """

    def isValid(self, s: str) -> bool:
        stack = []
        hash_map = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in hash_map.values():
                stack.append(i)
            elif i in hash_map.keys():
                if not stack or hash_map[i] != stack.pop():
                    return False
        return True if not stack else False

    """
    Linked List Cycle
    """


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution3:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

    """
    104. Maximum Depth of Binary Tree
    """


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution4:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    """
    530. Minimum Absolute Difference in BST
        """

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        answer = float("inf")
        q = deque([root])
        arr = []
        while q:
            current = q.popleft()
            arr.append(current.val)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        arr.sort()
        for i in range(1, len(arr)):
            answer = min(answer, arr[i] - arr[i - 1])
        return answer
