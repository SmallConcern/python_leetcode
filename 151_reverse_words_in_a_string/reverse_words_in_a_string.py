
def reverse_words(s):
    return '' if s is None or not s else ' '.join([word.strip()
                                                   for word in reversed(s.strip().split(' '))
                                                   if word.strip()])

class TestReverseWords(object):
    def test_reverse_words(self):
        assert reverse_words(None) == ''
        assert reverse_words('') == ''
        assert reverse_words(' ') == ''
        assert reverse_words('hello') == 'hello'
        assert reverse_words('the sky is blue') == 'blue is sky the'
        assert reverse_words('   a   b ') == 'b a'