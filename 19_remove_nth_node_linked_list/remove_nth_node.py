class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

    def remove_from_end(self, n):
        if n == 0:
            return
        current = self.head
        advanced = 0
        while current and advanced < n:
            advanced += 1
            current = current.next
        if advanced < n:
            return
        else:
            to_end = current
            previous = self.head
            current = self.head
            while to_end:
                to_end = to_end.next
                if current.next:
                    previous = current
                current = current.next
            if current == self.head:
                self.head = self.head.next
            elif not current:
                previous.next = None
            else:
                previous.next = current.next

    def __str__(self):
        out = ''
        current = self.head
        while current:
            out += str(current.val)
            current = current.next
        return out

class Solution(object):
    def removeNthFromEnd(self, head, n):
        ll = LinkedList()
        ll.head = head
        ll.remove_from_end(n)
        return ll.head


class TestRemoveNthNode(object):
    def test_remove_nth_node(self):
        ll = LinkedList()
        [ll.append(x) for x in range(5)]
        assert str(ll) == '01234'
        ll.remove_from_end(2)
        assert str(ll) == '0124'
        ll.remove_from_end(4)
        assert str(ll) == '124'
        ll.remove_from_end(0)
        assert str(ll) == '124'
        ll.remove_from_end(1)
        assert str(ll) == '12'
        ll.remove_from_end(1)
        assert str(ll) == '1'
        ll.remove_from_end(1)
        assert str(ll) == ''

