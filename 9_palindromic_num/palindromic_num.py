
def is_palindromic_num(n):
    if n < 0 or (n != 0 and n % 10 == 0): return False
    rev = 0
    while n > rev:
        rev = rev*10 + n%10
        n /= 10
    return n == rev or n == rev/10


class TestPalindromicNum(object):
    def test_palindromic_num(self):
        assert is_palindromic_num(12321)
        # assert is_palindromic_num(1111)
        # assert not is_palindromic_num(1233)
        # assert is_palindromic_num(1233321)