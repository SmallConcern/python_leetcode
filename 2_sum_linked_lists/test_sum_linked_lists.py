from sum_linked_lists import Solution
from sum_linked_lists import LinkedList

class TestLinkedList():
    def test_linked_list_append(self):
        ll = LinkedList()
        assert not ll.root
        ll.append(5)
        assert ll.root
        assert ll.root.val == 5
        ll.append(1)
        ll.append(9)
        assert ll.root.next.val == 1
        assert ll.root.next.next.val == 9

    def test_linked_list_from_num(self):
        ll = LinkedList.linked_list_from_num(519)
        assert ll.root.val == 5
        assert ll.root.next.val == 1
        assert ll.root.next.next.val == 9

    def test_linked_list_to_str(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(1)
        ll.append(9)
        assert LinkedList.linked_list_to_str(ll) == "519"

    def test_linked_list_to_reversed_num(self):
        ll = LinkedList.linked_list_from_num(519)
        assert LinkedList.linked_list_to_reversed_num(ll) == 915
        ll = LinkedList.linked_list_from_num(1)
        assert LinkedList.linked_list_to_reversed_num(ll) == 1

class TestSolution():
    def test_linked_list_from_num(self):
        l1 = LinkedList.linked_list_from_num(243)
        l2 = LinkedList.linked_list_from_num(564)
        root = Solution.addTwoNumbers(l1.root, l2.root)
        assert root.val == 7
        assert root.next.val == 0
        assert root.next.next.val == 8