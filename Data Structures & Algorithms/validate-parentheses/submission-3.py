class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack and c in [")", "}", "]"]:
                return False
            if (c == "]" and stack[-1] == "[") or (c == "}" and stack[-1] == "{") or (c == ")" and stack[-1] == "("):
                stack.pop()
            elif c in ["(", "{", "["]:
                stack.append(c)
            else:
                return False
        
        return len(stack) == 0