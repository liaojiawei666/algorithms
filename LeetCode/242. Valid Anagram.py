class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l1=list(s)
        l2=list(t)
        count={}
        for item in l1:
            count[item]=count.get(item,0)+1
        for item in l2:
            if item not in count or count[item]<0:
                return False
            count[item]-=1
            if count[item]==0:
                count.pop(item)
        if len(count)==0:
            return True
        else:
            return False

r=Solution().isAnagram("anagram","nagaram")
print(r)
