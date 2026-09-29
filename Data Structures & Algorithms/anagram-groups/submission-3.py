class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        check = {}
        for word in strs:
            word_array = [0] * 26
            for c in word:
                word_array[ord(c) - ord('a')] += 1
            if tuple(word_array) not in check:
                check[tuple(word_array)] = []
            check[tuple(word_array)].append(word)
        return list(check.values())