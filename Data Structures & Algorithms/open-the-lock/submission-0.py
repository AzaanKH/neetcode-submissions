class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        q = deque(['0000'])
        check = set(deadends)
        check.add('0000')
        steps = 0
        while q:
            steps += 1
            for _ in range(len(q)):
                curr = q.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(curr[i]) + j + 10) % 10)
                        next = curr[:i] + digit + curr[i+1:]
                        if next in check:
                            continue
                        if next == target:
                            return steps
                        q.append(next)
                        check.add(next)
        return -1