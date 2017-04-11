def isomorphic_strings(s1, s2):
    if len(s1) != len(s2):
        return False
    char_dict = {}
    s2_chars = set()
    for char_idx, char in enumerate(s1):
        if char not in char_dict:
            if s2[char_idx] not in s2_chars:
                char_dict[char] = s2[char_idx]
                s2_chars.add(s2[char_idx])
            else:
                return False
        elif char_dict[char] != s2[char_idx]:
            return False
    return True


class TestIsomorphicStrings(object):
    def test_isomorphic_strings(self):
        assert isomorphic_strings("egg", "add")
        assert not isomorphic_strings("foo", "bar")
        assert isomorphic_strings("paper", "title")
        assert not isomorphic_strings("ab", "aa")