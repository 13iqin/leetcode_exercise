class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


if __name__ == "__main__":
    s = Solution()
    k = "  hello world!  "
    k2 = "a good   example"
    res = s.reverseWords(k2)
    print(res)
