class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for c in path.split("/"):
            if c == '..':
                if stack:
                    stack.pop()
            if c == '.' or c == "" or c == "..":
                continue
            stack.append(c)
        return "/" + "/".join(stack)