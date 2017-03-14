def _balloon_burst_max_r(balloon_arr, value):
    if not balloon_arr:
        return 0
    elif len(balloon_arr) == 1:
        return value + balloon_arr[0]
    max_val = 0
    for x in range(len(balloon_arr)):
        val = 0
        if x > 0 and x < len(balloon_arr)-1:
            val = balloon_arr[x-1] * balloon_arr[x] * balloon_arr[x+1]
        elif x > 0:
            val = balloon_arr[x-1] * balloon_arr[x]
        elif x < len(balloon_arr) - 1:
            val = balloon_arr[x] * balloon_arr[x+1]
        max_val = max(_balloon_burst_max_r(balloon_arr[:x] + balloon_arr[x+1:], value + val), max_val)
    return max_val

def balloon_burst_max_r(balloon_arr):
    return _balloon_burst_max_r(balloon_arr, 0)

def balloon_burst_max_dp(balloon_arr):
    matrix = []
    for x in xrange(len(balloon_arr)): matrix.append([0] * len(balloon_arr))
    print matrix


class Solution(object):
    def maxCoins(self, nums):
        return balloon_burst_max_r(nums)

class TestBalloonBurstMax(object):
    def test_balloon_burst_max_r(self):
        assert balloon_burst_max_r([3,1,5,8]) == 167

    def test_balloon_burst_max_dp(self):
        assert balloon_burst_max_dp([3,1,5,8]) == 167
        print balloon_burst_max_dp([35, 16, 83, 87, 84, 59, 48, 41, 20, 54])
        # import random
        # print balloon_burst_max_r([random.randint(0,100) for _ in xrange(500)])