
def convert_to_zig_zag(input_str, rows):
    if not input_str:
        return ''
    elif rows == 1:
        return input_str
    else:
        lines = [''] * rows
        row = 0
        down = True
        for char in input_str:
            if down:
                lines[row] += char
                if row == rows-1:
                    down = False
                    row -= 1
                else:
                    row += 1
            else:
                lines[row] += char
                if row == 0:
                    down = True
                    row += 1
                else:
                    row -= 1
        lines = [l for l in lines if l]
        return ''.join(lines)

class Solution(object):
    def convert(self, s, numRows):
        return convert_to_zig_zag(s, numRows)


class TestZigZagConversion(object):
    def test_zig_zag_conversion(self):
        assert convert_to_zig_zag("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
        assert convert_to_zig_zag("C", 1) == "C"
        assert convert_to_zig_zag("CAS", 1) == "CAS"
        assert convert_to_zig_zag("CAS", 2) == "CSA"
        assert convert_to_zig_zag("A", 2) == "A"
        assert convert_to_zig_zag("AB", 2) == "AB"