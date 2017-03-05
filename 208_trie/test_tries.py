from tries import TrieNode
from tries import Trie

class TestTrieNode():
    def test_trie_node(self):
        tn = TrieNode()
        assert tn
        assert not tn.char
        assert not tn.terminator
        assert len(tn.children.keys()) == 0
        tn = TrieNode('a', True)
        tn.children['b'] = TrieNode('b', True)
        assert tn.char == 'a'
        assert tn.terminator == True
        assert 'b' in tn.children
        assert tn.children['b'].char == 'b'

class TestTrie():
    def test_trie_basic_insert(self):
        tn = Trie()
        assert tn.root
        tn.insert("f")
        assert 'f' in tn.root.children
        tn.insert("f")
        assert 'f' in tn.root.children
        tn.insert("ha")
        assert 'h' in tn.root.children
        assert not tn.root.children['h'].terminator
        assert 'a' in tn.root.children['h'].children
        tn.insert("h")
        assert tn.root.children['h'].terminator

    def test_trie_search(self):
        tn = Trie()
        tn.insert("hello")
        assert tn.search("hello")
        assert not tn.search("hell")
        assert not tn.search("hellop")
        tn.insert("hellop")
        assert tn.search("hellop")
        assert not tn.search('')

    def test_trie_prefix(self):
        tn = Trie()
        tn.insert("hello")
        assert tn.startsWith("hello")
        assert tn.startsWith("hell")
        assert tn.startsWith("h")
        tn.insert("banana")
        tn.insert("ban")
        assert tn.startsWith("ban")
        assert tn.startsWith('')
        assert not tn.startsWith('a')