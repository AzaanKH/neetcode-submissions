class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                parts = []
                print(stack)
                while stack and not isinstance(stack[-1], int):
                    next = stack.pop()
                    if next != '[':
                        parts.append(next)
                parts.reverse()
                digit = stack.pop()
                stack.append(digit * "".join(parts))
            elif c.isdigit():
                if stack and isinstance(stack[-1], int):
                    stack[-1] = stack[-1] * 10 + int(c)
                else:
                    stack.append(int(c))
            else:
                stack.append(c)
        return "".join(stack)