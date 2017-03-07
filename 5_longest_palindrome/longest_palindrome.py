def find_longest_palindrome(input_str):
    if len(input_str) == 0:
        return ''
    elif len(input_str) == 1:
        return input_str
    longest_palindrome = ''
    for start in xrange(0, len(input_str)):
        left = right = start
        while right < len(input_str)-1 and input_str[right+1] == input_str[right]:
            right += 1
        while right < len(input_str)-1 and left > 0 and input_str[left-1] == input_str[right+1]:
            right += 1
            left -= 1
        if right - left + 1 > len(longest_palindrome):
            longest_palindrome = input_str[left:right+1]
    return longest_palindrome

class Solution(object):
    def longestPalindrome(self, s):
        return find_longest_palindrome(s)

class TestLongestPalindrome(object):
    def test_find_longest_palindrome(self):
        assert find_longest_palindrome("babad") == "bab"
        assert find_longest_palindrome("cbbd") == "bb"
        assert find_longest_palindrome("dbbd") == "dbbd"
        assert find_longest_palindrome("abcdefghihgfedcba") == "abcdefghihgfedcba"
        assert find_longest_palindrome("abcdefghiihgfedcba") == "abcdefghiihgfedcba"
        assert find_longest_palindrome("banana") == "anana"
        assert find_longest_palindrome("aaabaaaa") == "aaabaaa"
        assert find_longest_palindrome("bb") == "bb"