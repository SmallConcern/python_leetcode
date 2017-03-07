
def find_longest_palindrome(input_str):
    longest_palindrome = ''
    for start in xrange(1, len(input_str)-2):
        distance_from_end = min(len(input_str)-1-start, start)
        right_modifier = 0
        if input_str[start] == input_str[start+1]:
            right_modifier = 1
            longest_palindrome = max(longest_palindrome, input_str[start:start+2])
        for j in xrange(1, distance_from_end+1):
            if input_str[start-j] != input_str[start+j+right_modifier]:
                break
            else:
                palindrome = input_str[start - j:start + j + 1 + right_modifier]
                if len(palindrome) > len(longest_palindrome):
                    longest_palindrome = palindrome
    return longest_palindrome


class Solution(object):
    def longestPalindrome(self, s):
        return find_longest_palindrome(s)

class TestLongestPalindrome(object):
    def test_find_longest_palindrome(self):
        # assert find_longest_palindrome("babad") == "bab"
        # assert find_longest_palindrome("cbbd") == "bb"
        # assert find_longest_palindrome("dbbd") == "dbbd"
        # assert find_longest_palindrome("abcdefghihgfedcba") == "abcdefghihgfedcba"
        # assert find_longest_palindrome("abcdefghiihgfedcba") == "abcdefghiihgfedcba"
        # assert find_longest_palindrome("banana") == "anana"
        assert find_longest_palindrome("aaabaaaa") == "aaabaaa"