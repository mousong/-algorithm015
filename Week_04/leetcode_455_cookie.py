class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort()
        s.sort()
        g_len = len(g)
        s_len = len(s)

        i = 0
        j = 0
        while i < g_len and j < s_len:
            if g[i] <= s[j]:
                j += 1
                i += 1
                res += 1
            else:
                j += 1
        return res