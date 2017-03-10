class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

    def remove_with_previous(self, previous, remove):
        if not previous:
            self.head = remove.next
        else:
            previous.next = remove.next
        return remove

    def insert_after_node(self, insert_after, insert):
        previous_next = insert_after.next
        insert_after.next = insert
        insert.next = previous_next

    def odd_even_shuffle(self):
        if not self.head or not self.head.next:
            return
        current_index = 2
        insert_after = self.head
        previous = insert_after
        current = previous.next
        while current:
            if current_index % 2 != 0:
                removal = self.remove_with_previous(previous, current)
                current = previous.next
                self.insert_after_node(insert_after, removal)
                insert_after = removal
            else:
                previous = current
                current = current.next
            current_index += 1

    def __str__(self):
        str_buff = ""
        current = self.head
        while current:
            str_buff += (str(current.val))
            current = current.next
        return str_buff

class Solution(object):
    @staticmethod
    def oddEvenList(head):
        linked_list = LinkedList()
        linked_list.head = head
        linked_list.odd_even_shuffle()
        return linked_list.head

class TestOddEvenLinkedList():
    def test_odd_even_linked_list(self):
        linked_list = LinkedList()
        for x in range(1,7): linked_list.append(x)
        assert str(linked_list) == "123456"
        linked_list.odd_even_shuffle()
        assert str(linked_list) == "135246"

class TestLinkedListImpl():
    def test_linked_list_append(self):
        linked_list = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        assert linked_list.head.val == 1
        assert linked_list.head.next.val == 2
        assert not linked_list.head.next.next