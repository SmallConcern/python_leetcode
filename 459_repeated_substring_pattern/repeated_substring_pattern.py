def repeated_substrings(s):
    for x in range(len(s)/2):
        if len(s) % (x+1) == 0 and s[:x+1]*(len(s)/(x+1)) == s:
            return True
    return False

class TestRepeatedSubstringPattern(object):
    def test_repeated_substring_pattern(self):
        assert repeated_substrings("abab")
        assert not repeated_substrings("aba")
        assert repeated_substrings("abcabcabcabc")