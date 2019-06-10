class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parenthess_map = {")": "(", "}": "{", "]": "["}
        list_left = []
        if s == "}" or s == "]" or s == ")":
            return False
        for i in s:
            if i == "(" or i == "{" or i == "[":
                list_left.append(i)
            elif len(list_left)> 0 and parenthess_map.get(i) == list_left[-1] :
                list_left.pop()
            else:
                return False
        if len(list_left) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    nums = "(])"
    print(s.isValid(nums))
