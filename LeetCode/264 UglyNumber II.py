# Write a progranext_item to find the n-th ugly nunext_itember.
#
# Ugly nunext_itembers are positive nunext_itembers whose prinext_iteme factors only include 2, 3, 5.
#
# Exanext_itemple:
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly nunext_itembers.
# Note:
#
# 1 is typically treated as an ugly nunext_itember.
# n does not exceed 1690.

class Solution:
    ugly = [1]
    ugly2, ugly3, ugly5, cnt = 0, 0, 0, 0
    while cnt < 1690:
        next_item = min(2 * ugly[ugly2], 3 * ugly[ugly3], 5 * ugly[ugly5])
        ugly.append(next_item)
        if next_item == 2 * ugly[ugly2]:
            ugly2 += 1
        if next_item == 3 * ugly[ugly3]:
            ugly3 += 1
        if next_item == 5 * ugly[ugly5]:
            ugly5 += 1
        cnt += 1

    def nthUglyNumber(self, n):
        return self.ugly[n - 1]
# m1690=2125764000   #>10**10
# # s = Solution()
# # # print(s.nthUglyNumber(10))
# # print(s.ugly)
# import time
# start=time.clock()
# for i in range(10**8):
#     pass
# print(time.clock()-start)