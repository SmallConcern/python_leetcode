import sys

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "ListNode(x={}, {})".format(self.val, self.next)

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

    def __str__(self):
        str_buff = ""
        current = self.head
        while current:
            str_buff += (str(current.val)) + ","
            current = current.next
        return str_buff

class SortedListsMerger(object):
    @staticmethod
    def get_sorted_linked_list_no_external_space(lists):
        lists = [l for l in lists if l]
        head = None
        append_pointer = None
        while lists:
            min_node = ListNode(sys.maxint)
            min_idx = -1
            for i, node in enumerate(lists):
                if node and node.val < min_node.val:
                    min_node = node
                    min_idx = i
            if min_idx == -1:
                return
            if not head:
                append_pointer = min_node
                head = append_pointer
            else:
                append_pointer.next = min_node
                append_pointer = min_node
            lists[min_idx] = min_node.next
            if not min_node.next:
                del lists[min_idx]
        return head

    @staticmethod
    def get_sorted_linked_list(lists): # this came straight from leetcode solutions, not mine
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h)  # only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next

        return dummy.next


class Solution(object):
    def mergeKLists(self, lists):
        return SortedListsMerger.get_sorted_linked_list(lists)


class TestMergeKSortedLists(object):
    def generate_k_lists(self, k, data_range=(-100, 100), list_size=10):
        import random
        lists = []
        for x in xrange(k):
            data_set = [random.randint(*data_range) for foo in xrange(list_size)]
            ll = LinkedList()
            for val in sorted(data_set): ll.append(val)
            lists.append(ll.head)
        return lists

    def test_edge_cases(self):
        lists = [None, ListNode(1)]
        head = SortedListsMerger.get_sorted_linked_list(lists)
        assert head.val == 1
        assert head.next == None

    def test_merge_k_sorted_lists(self):
        lists = self.generate_k_lists(5)
        head = SortedListsMerger.get_sorted_linked_list(lists)
        ll = LinkedList(head)
        print ll

    def test_stress_test(self):
        lists = self.generate_k_lists(1000, data_range=(-10000, 100000), list_size=1000)
        head = SortedListsMerger.get_sorted_linked_list(lists)
        ll = LinkedList(head)
        print ll
