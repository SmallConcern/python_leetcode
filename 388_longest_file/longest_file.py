from collections import defaultdict


def longest_file_path(file_path):
    fs_items = file_path.split('\n')
    path_lengths = defaultdict(int)
    max_len = 0
    for item in fs_items:
        name = item.replace('\t', '')
        depth = len(item) - len(name)
        if '.' in name:
            max_len = max(max_len, path_lengths[depth] + len(name))
        else:
            path_lengths[depth + 1] = path_lengths[depth] + len(name) + 1
    return max_len


class TestLongestFilePath(object):
    def test_longest_file_path(self):
        file_path = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
        assert longest_file_path(file_path) == 32