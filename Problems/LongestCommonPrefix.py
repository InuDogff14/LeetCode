class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs:
            while string[:len(prefix)] != prefix:
                 prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix