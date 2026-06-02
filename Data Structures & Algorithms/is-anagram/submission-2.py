class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s) == len(t): # Tienen mismo numero total de caracteres
            if set(s) == set(t): # Tienen los mismas caracteres
                list_s = list(s)
                list_t = list(t)
                for s_char in list_s:
                    dict_s[s_char] = dict_s.get(s_char, 0) + 1
                for t_char in list_t:
                    dict_t[t_char] = dict_t.get(t_char, 0) + 1
                for char in set(s):
                    if dict_t[char] != dict_s[char]:
                        return False
                return True
            else:
                return False
        else:
            return False
