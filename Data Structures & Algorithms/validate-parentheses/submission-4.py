class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {")": "(", "}": "{", "]": "["}
        valid = []
        if len(s)<=1:
            return False

        for i in s:
            if i in ["(", "{", "["]:
                valid.append(i)
            else:
                if len(valid)==0:
                    return False
                last_bracket = valid.pop()
                if last_bracket != bracket_map[i]:
                    return False


        return len(valid)==0

        
