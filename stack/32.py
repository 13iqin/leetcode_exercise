class Solution(object):
    def evalRPN(self, tokens):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                if token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
                elif token == '*':
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack.pop()


if __name__ == "__main__":
    s = Solution()
    nums = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(s.evalRPN(nums))
