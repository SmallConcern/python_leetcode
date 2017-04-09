class Solution(object):
    @staticmethod
    def find_content_children(g, s):
        if g is None or s is None:
            raise TypeError('Invalid inputs.')
        g = sorted(g)
        s = sorted(s)
        greed_idx, cookie_idx = 0, 0
        while greed_idx < len(g) and cookie_idx < len(s):
            if g[greed_idx] <= s[cookie_idx]:
                greed_idx += 1
            cookie_idx += 1
        return greed_idx


class TestAssignCookies(object):
    def test_assign_cookies(self):
        assert Solution.find_content_children([1, 1, 1, 1], [1, 1, 1, 1]) == 4
        assert Solution.find_content_children([2, 2, 2, 2], [1, 1, 1, 1]) == 0
        assert Solution.find_content_children([1, 2, 3, 4], [1, 2, 3]) == 3
        assert Solution.find_content_children([10, 12, 5, 5, 9], [5, 10, 4, 8]) == 3