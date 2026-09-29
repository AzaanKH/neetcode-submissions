class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        for string in strings:
            key = tuple((ord(string[i]) - ord(string[i-1])) % 26 for i in range(1, len(string)))
            check[key].append(string)
        return list(check.values())