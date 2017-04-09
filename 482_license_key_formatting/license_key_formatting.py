def format_license_key(license_key, k):
    if license_key is None or k is None:
        raise TypeError('Invalid inputs provided: {}, {}'.format(license_key, k))
    license_key = license_key.replace('-', '').upper()
    if len(license_key) <= k: return license_key
    count = 0
    for char_idx in range(len(license_key), -1, -1):
        if char_idx and count and count % k == 0:
            license_key = license_key[:char_idx] + '-' + license_key[char_idx:]
        count += 1
    return license_key


class Solution(object):
    def licenseKeyFormatting(self, s, k):
        return format_license_key(s, k)


class TestLicenseKeyFormatting(object):
    def test_license_key_formatting(self):
        assert format_license_key('2-4A0r7-4k', 3) == '24-A0R-74K'
        assert format_license_key('2-4A0r7-4k', 4) == '24A0-R74K'
        assert format_license_key('a0001afds-', 4) == 'A-0001-AFDS'