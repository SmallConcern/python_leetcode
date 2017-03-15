class Solution(object):
    def maxSubArray(self, nums):
        dp = [nums[0],0]
        m = dp[0]

        for x in range(1, len(nums)):
            dp[1] = max(nums[x] + dp[0], nums[x])
            m = max(m, dp[1])
            dp[0] = dp[1]

        return m


class TestMaximumSubarray(object):
    def test_maximum_subarray(self):
        s = Solution()
        assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
        assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -7, 100]) == 100