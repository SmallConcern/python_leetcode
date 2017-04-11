def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    list_s = list(s)
    i, j = 0, len(s)-1
    while i < j:
        if list_s[i] in vowels and list_s[j] in vowels:
            list_s[i], list_s[j] = list_s[j], list_s[i]
            i += 1
            j -= 1
        if list_s[i] not in vowels:
            i += 1
        if list_s[j] not in vowels:
            j -= 1
    return ''.join(list_s)

class TestReverseVowels(object):
    def test_reverse_vowels(self):
        assert reverse_vowels("") == ""
        assert reverse_vowels("foo") == "foo"
        assert reverse_vowels("flm") == "flm"
        assert reverse_vowels("hello") == "holle"
        assert reverse_vowels("leetcode") == "leotcede"
        assert reverse_vowels("lypvghio") == "lypvghoi"