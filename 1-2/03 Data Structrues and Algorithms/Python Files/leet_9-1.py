class Solution(object):

    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        total = 0
        for i in words:
            if i.startswith(pref) :
                total += 1
        return total
    
sol = Solution()

l1 = ["hello","help","hi","heat","owl"]
print(sol.prefixCount(l1, "he"))