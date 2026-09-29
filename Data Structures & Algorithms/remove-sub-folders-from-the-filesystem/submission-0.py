class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end = False
    

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()
        res = []
        folder.sort()
        for word in folder:
            node = root
            include = True
            for c in word.strip("/").split("/"):
                if node.end == True:
                    include = False
                    break
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            if include == True:
                node.end = True
                res.append(word)
        return res
