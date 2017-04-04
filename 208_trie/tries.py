class TrieNode(object):
    def __init__(self, char=None, terminator=False):
        self.char = char
        self.children = {}
        self.terminator = terminator


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in list(word):
            if char in node.children:
                node = node.children.get(char)
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.terminator = True

    def search(self, word, complete_word=True):
        node = self.root
        for char in list(word):
            if char in node.children:
                node = node.children.get(char)
            else:
                return False
        return node.terminator if complete_word else True

    def startsWith(self, prefix):
        return self.search(prefix, complete_word=False)