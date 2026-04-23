class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        NUM_LETTERS = 26

        for s in strs:
            count = [0] * NUM_LETTERS

            for c in s:
                count[ord(c) - ord('a')] += 1

            if tuple(count) not in anagrams:
                anagrams[tuple(count)] = []
            anagrams[tuple(count)].append(s)

        return list(anagrams.values())