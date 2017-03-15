def reverse_int(n):
    new_num = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while n != 0:
        new_num *= 10
        new_num += n % 10
        n /= 10
    if new_num > 2147483647:
        return 0
    else:
        return new_num * sign


class Solution(object):
    def reverse(self, x):
        return reverse_int(x)


class TestReverseInt(object):
    def test_reverse_int(self):
        assert reverse_int(123) == 321
        assert reverse_int(-123) == -321
        assert reverse_int(1000000003) == 0
        assert reverse_int(1534236469) == 9646324351