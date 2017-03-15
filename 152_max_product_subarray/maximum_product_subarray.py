class Solution(object):
    def maxProduct(self, nums):
        dp = [nums[0],0]
        dp_min = [nums[0], 0]
        m = dp[0]

        for x in range(1, len(nums)):
            dp[1] = max(nums[x] * dp[0], nums[x], nums[x] * dp_min[0])
            dp_min[1] = min(nums[x] * dp_min[0], nums[x], nums[x] * dp[0])
            m = max(m, dp[1])
            dp[0], dp_min[0] = dp[1], dp_min[1]

        return m


class TestMaximumSubarray(object):
    def test_maximum_subarray(self):
        s = Solution()
        assert s.maxProduct([-1,-2,-9,-6]) == 108
        assert s.maxProduct([2, 3, -2, 4, 2]) == 8
        assert s.maxProduct([2, -1, 3, -2, 4, -2]) == 48
        assert s.maxProduct([2, 3, -2, 4, 2, -1, 9]) == 864
        assert s.maxProduct([-2,3,-4]) == 24
        assert s.maxProduct([-2, 1, -3, 4, 50, 2, 1, -7, 100]) == 840000