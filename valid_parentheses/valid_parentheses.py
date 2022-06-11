class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = { "(":")", "[":"]", "{":"}" }
        open_bracket = set([ "(", "[", "{" ])
        stack = []
        for i in s:
            if i in open_bracket:
                stack.append(i)
            elif stack and i == brackets_map[stack[-1]]:
                    stack.pop()
            else:
                return False
        return stack == []