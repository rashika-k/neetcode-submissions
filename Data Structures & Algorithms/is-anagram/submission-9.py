
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}
        if len(s) == len(t):
            for i in s:
                if i in ss:
                    ss[i] += 1
                else:
                    ss[i] = 1

            for i in t:
                if i in tt:
                    tt[i] += 1
                else:
                    tt[i] = 1

            if ss == tt:
                return True
        return False
            