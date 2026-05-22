# class Solution:
#     def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         s1 = [i for i in s1]
#         s2 = [i for i in s2]
#         a = s1.copy()
#         b = s2.copy()
#         if a.sort() == b.sort():
#             for i in range(len(s1)):
#                 for j in range(i, len(s1)):
#                     c = s1.copy()
#                     k = s1[i]
#                     s1[i] = s1[j]
#                     s1[j] = k
#                     if s1 == s2:
#                         return True
#                     else:
#                         s1 = c
#         return False

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        diff = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff += 1
            if diff > 2:
                return False
        return True


if __name__ == "__main__":
    s1 = "bank"
    s2 = "kanb"
    s = Solution()
    print(s.areAlmostEqual(s1, s2))