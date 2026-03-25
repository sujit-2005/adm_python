class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        first=-1
        sec=-1
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                if first==-1:
                    first=i
                elif sec==-1:
                    sec=i
                else:
                    return False
        if sec==-1:
            return False
        return s1[first]==s2[sec] and s1[sec]==s2[first]