from longest_substring import LongestSubstring


class TestLongestSubstring():
    def test_longest_substring_invalid_inputs(self):
        LongestSubstring.find_longest_substring('') == 0

    def test_longest_substring(self):
        assert LongestSubstring.find_longest_substring('c') == 1
        assert LongestSubstring.find_longest_substring('dvdf') == 3
        assert LongestSubstring.find_longest_substring('dvodf') == 4
        assert LongestSubstring.find_longest_substring('bbbbbb') == 1
        assert LongestSubstring.find_longest_substring('abcabcbb') == 3
        assert LongestSubstring.find_longest_substring('pwwkew') == 3