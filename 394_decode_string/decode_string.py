from string import ascii_lowercase

def decode_string(enc_str):
    if not enc_str:
        return ''
    l_brackets = []
    digit_starts = []
    parse_digit_start, idx = -1, 0
    done = False
    while not done:
        if enc_str[idx] == ']':
            l_bracket_pos = l_brackets.pop()
            new_str = enc_str[l_bracket_pos + 1:idx]
            digit_start = digit_starts.pop()
            multiple = int(enc_str[digit_start:l_bracket_pos])
            enc_str = enc_str[:digit_start] + new_str * multiple + enc_str[idx + 1:]
            idx = idx - (idx-digit_start) + len(new_str) * multiple - 1
        else:
            if enc_str[idx] == '[':
                digit_starts.append(parse_digit_start)
                parse_digit_start = -1
                l_brackets.append(idx)
            elif enc_str[idx] not in ascii_lowercase and parse_digit_start == -1:
                parse_digit_start = idx
            idx += 1
        if idx >= len(enc_str):
            done = True
    return enc_str



class TestDecodeString(object):
    def test_decode_string(self):
        assert decode_string('') == ''
        assert decode_string("ab10[c]") == "abcccccccccc"
        assert decode_string("3[a]2[bc]") == "aaabcbc"
        assert decode_string("3[a2[c]]") == "accaccacc"
        assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
        assert decode_string("2[2[b]]") == "bbbb"