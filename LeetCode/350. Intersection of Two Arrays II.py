class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        count1 = {}
        count2 = {}
        result = list()
        for item in nums1:
            count1[item] = count1.get(item, 0) + 1
        for item in nums2:
            count2[item] = count2.get(item, 0) + 1
        k = count1.keys() & count2.keys()
        for item in k:
            c = min(count1[item], count2[item])
            a = [item for i in range(c)]
            result.extend(a)
        return result
