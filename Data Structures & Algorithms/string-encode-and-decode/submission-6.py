class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for st in strs:
            result += str(len(st)) + "#" + st
        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        decode_list = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decode_list.append(s[i:j])
            i = j
        return decode_list
