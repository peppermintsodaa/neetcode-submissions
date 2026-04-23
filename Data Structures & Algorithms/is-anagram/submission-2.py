class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count_s[s[i]] = count_s.setdefault(s[i], 0) + 1
            count_t[t[i]] = count_t.setdefault(t[i], 0) + 1

        return count_s == count_t