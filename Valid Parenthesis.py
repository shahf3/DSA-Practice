def isValid(self, s: str) -> bool:

        dic = {")": "(", "]": "[", "}": "{"}
        stack = []

        for elem in s:
            if elem in dic:
                if not stack or stack[-1] != dic[elem]:
                    return False
                
                stack.pop()
            else:
                stack.append(elem)
        
        return len(stack) == 0