class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counting_s = {}
        counting_t = {}
        for char in s:
            if char not in counting_s:
                counting_s[char] = 1
            else:
                counting_s[char] += 1

        for char in t:
            if char not in counting_t:
                counting_t[char] = 1
            else:
                counting_t[char] += 1

        return counting_s == counting_t