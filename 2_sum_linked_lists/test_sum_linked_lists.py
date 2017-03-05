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

# class TestSumLinkedLists():
#     def test_linked_list_from_num(self):
