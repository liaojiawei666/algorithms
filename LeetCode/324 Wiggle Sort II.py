# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
#
# Example 1:
#
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6].
# Example 2:
#
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2].
# Note:
# You may assume all input has valid answer.
#
# Follow Up:
# Can you do it in O(n) time and/or in-place with O(1) extra space?

class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        ln=len(nums)
        if ln>=2:
            mid=(ln-1)//2
            left=1
            if mid%2==0:
                right=mid+2
            else:
                right=mid+1
            while left<=mid:
                nums[left],nums[right]=nums[right],nums[left]
                left,right=left+2,right+2

        l = len(nums)
        self.kth(nums, 0, l - 1, (l + 1) // 2)
        self.rearrange(nums)
        print(nums)

    def rearrange(self, A):
        # A满足index小于len(A)//2的值小于A[len(A)//2] index大于len(A)//2的值大于A[len(A)//2]
        # 现在需要排成index%2==1的数大于相邻的两位数
        la = len(A)
        if la >= 2:
            if la % 2 == 0:
                left, right = 1, la - 2
            else:
                left, right = 1, la - 1
            while left < right:
                A[left], A[right] = A[right], A[left]
                left, right = left + 2, right - 2

    def kth(self, A, l, r, k):
        if l == r:
            return A[l]
        else:
            p = self.partition(A, l, r)
            q = p - l + 1
            if q == k:
                return A[p]
            elif q < k:
                return self.kth(A, p + 1, r, k - q)
            else:
                return self.kth(A, l, p - 1, k)

    def partition(self, A, p, r):
        tmp = A[r]
        left, right = p, r
        while left < right:
            while left < right and A[left] <= tmp:
                left += 1
            A[right] = A[left]
            while left < right and A[right] >= tmp:
                right -= 1
            A[left] = A[right]
        A[left] = tmp
        return left


import random

s = Solution()
x = [random.randint(0, 100) for i in range(11)]
# x=[35, 47, 26, 3, 98, 29, 0, 62, 57, 99]
print(x)
s.wiggleSort(x)
