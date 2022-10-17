class Solution:
    def findAnagrams(self, s: str, p: str) -> list:

        # [1: 1 + 3]
        # i: i + len(p)
        # cbaebabacd
        # cbaebab acd
        # cba
        # i = 0
        # i = 1 => bae
        # answer.append(i)
        answer = []
        for i in range(len(s) - len(p)):
            if self.is_anagram(s[i:i + len(p)], p):
                answer.append(i)
        return answer

    @staticmethod
    def is_anagram(first: str, second: str) -> bool:
        p_list = list(second)
        for letter in first:
            if letter in p_list:
                p_list.remove(letter)

        return not bool(p_list)

print(Solution().findAnagrams("cbaebabacd", "abc"))