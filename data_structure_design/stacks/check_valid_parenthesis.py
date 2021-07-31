class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        for character in s:
            if character in ['(','[','{']:
                stack_list.append(character)
            elif character == ')':
                try:
                    if stack_list.pop() != '(':
                        return False
                except:
                    return False
            elif character == ']':
                try:
                    if stack_list.pop() != '[':
                        return False
                except:
                    return False
            elif character == '}':
                try:
                    if stack_list.pop() != '{':
                        return False
                except:
                    return False
            else:
                return False
        if len(stack_list) == 0:
            return True
        else: return False
                
        
