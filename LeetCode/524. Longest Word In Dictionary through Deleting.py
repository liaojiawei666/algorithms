# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
#
# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# Output:
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]
#
# Output:
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.

# class Solution:
#     def findLongestWord(self, s, d):
#         """
#         :type s: str
#         :type d: List[str]
#         :rtype: str
#         """
#         result = ""
#         ls = len(s)
#         maxlen = 0
#         for item in d:
#             if len(item) < maxlen:
#                 continue
#             i = 0
#             flag = 0
#             for c in item:
#                 while i < ls and s[i] != c:
#                     i += 1
#                 i+=1
#                 if i == ls+1:
#                     flag = 1
#                     break
#             if flag==0 :
#                 if len(item)>maxlen or item<result:
#                     result=item
#                     maxlen=len(result)
#         return result
class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if len(s) == 0:
            return ''

        init_pos = [-2 for _ in range(26)]
        indexMatrix = [init_pos.copy()]
        for i in range(len(s) - 1, -1, -1):
            init_pos[ord(s[i]) - 97] = i
            indexMatrix.insert(0, init_pos.copy())
        ans = ''
        print(indexMatrix[-1])
        for word in d:
            if len(word) < len(ans):
                continue
            beginId = 0
            for w in word:
                beginId = indexMatrix[beginId][ord(w) - 97] + 1
                # print(w, beginId)
                if beginId == -1:
                    break
            else:
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word

        return ans
s = "bab"
d = ["ba","ab","a","b"]
x=Solution().findLongestWord(s,d)
print(x)
