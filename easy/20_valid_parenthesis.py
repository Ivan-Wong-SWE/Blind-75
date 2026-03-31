# Another solve using dictionary, use values method as well as a list as a makeshift stack 
class Solution(object):
    def isValid(self, s):
        stack = []
        if len(s) % 2 != 0:
            return False
        
        dict = {")": "(", "}": "{", "]": "["}
        for iter in s:
            if iter in map.values():
            # if iter == "(" or iter == "{" or iter == "[":
                stack.append(iter)
                continue
            elif iter in map:
                if not stack or map[iter] != stack.pop():
                    return False

        return len(stack) == 0