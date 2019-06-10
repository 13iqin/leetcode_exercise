class Solution:
    def maxSlidingWindow(self, nums, k):
        ans = []
        from collections import deque
        queue = deque()
        for i in range(len(nums)):
            while queue and queue[0] < i - k + 1:
                queue.popleft()
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans


if __name__ == "__main__":
    s = Solution()
    nums, k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    print(s.maxSlidingWindow(nums, k))
