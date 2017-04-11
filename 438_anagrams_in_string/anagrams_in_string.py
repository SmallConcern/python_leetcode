from collections import Counter

def anagrams_in_string(s, p):
    if not s or not p or len(s) < len(p):
        return []
    anagram_counts = Counter(p)
    string_counts = Counter(s[0:len(p)])
    anagram_positions = [] if anagram_counts != string_counts else [0]
    for j in range(len(p), len(s)):
        if string_counts[s[j-(len(p))]] > 1:
            string_counts[s[j - (len(p))]] -= 1
        else:
            del string_counts[s[j - (len(p))]]
        string_counts[s[j]] += 1
        if anagram_counts == string_counts:
            anagram_positions.append(j-(len(p)-1))
    return anagram_positions

class TestAnagramsInString(object):
    def test_anagrams_in_string(self):
        assert anagrams_in_string("", "") == []
        assert anagrams_in_string("foo", "") == []
        assert anagrams_in_string("", "foo") == []
        assert anagrams_in_string("abcd", "d") == [3]
        assert anagrams_in_string("foo", "foob") == []
        assert anagrams_in_string("cbaebabacd", "abc") == [0, 6]
        assert anagrams_in_string("abab", "ab") == [0, 1, 2]