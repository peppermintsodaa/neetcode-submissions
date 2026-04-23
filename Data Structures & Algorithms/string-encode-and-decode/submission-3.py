class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        last_i = 0
        num = 0
        ans = []

        for i in range(len(s)):
            if s[i] == '#' and s[i-1].isdigit():
                n = int(s[last_i:i])
                last_i = i+n+1
                ans.append(s[i+1:last_i])

        return ans
