class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        if not strs:
            return [[""]]
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in check:
                check[tuple(count)] = []
            check[tuple(count)].append(word)
            
        return list(check.values())