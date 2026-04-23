class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = dict()

        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1

        for c in t:
            if c in seen:
                seen[c] -= 1
    
        for num in seen.values():
            if num > 0:
                return False

        return True