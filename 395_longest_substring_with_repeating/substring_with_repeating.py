from collections import Counter


def _longest_substring(s, start, end, k):
    if end - start < k:
        return 0
    counts = Counter(s)
    for idx in range(start, end):
        if counts[s[idx]] < k:
            return max(_longest_substring(s, start, idx, k), _longest_substring(s, idx + 1, end, k))
    return end - start


def longest_substring(s, k):
    return _longest_substring(s, 0, len(s), k)


class TestSubstringWithRepeating(object):
    def test_substring_with_repeating(self):
        assert longest_substring("aaabb", 3) == 3
        assert longest_substring("ababbc", 2) == 5