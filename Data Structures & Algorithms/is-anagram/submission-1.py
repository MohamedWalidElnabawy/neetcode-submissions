class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_S = {}
        freq_T = {}
        for char in s:
            index = ord(char) - ord('a')
            freq_S[index] = freq_S.get(index, 0) + 1
        for char in t:
            index = ord(char) - ord('a')
            freq_T[index] = freq_T.get(index, 0) + 1

        return freq_S == freq_T