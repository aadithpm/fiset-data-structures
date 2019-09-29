from linked_list.linked_list import DoublyLinkedList
import unittest

class DoublyLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = DoublyLinkedList()
        self.ll.add(10)
        self.ll.add(5)
        self.ll.add(15)
    
    def test_head_and_tail(self):
        self.assertEqual(None, self.ll.head.prev)
        self.assertEqual(None, self.ll.tail.next)

    def test_next_and_prev(self):
        mid_node = self.ll.head.next

        self.assertEqual(mid_node.prev, self.ll.head)
        self.assertEqual(mid_node.next, self.ll.tail)

    def test_clear(self):
        self.ll.clear()

        self.assertEqual(self.ll.size(), 0)
        self.assertFalse(self.ll.head)
        self.assertFalse(self.ll.tail)

    def test_adding_element_adds_at_end_and_changes_tail(self):
        self.ll.add(25)

        self.assertEqual(self.ll.tail.data, 25)

    def test_adding_element_at_first_changes_head(self):
        old_head = self.ll.head

        self.ll.add_first(50)

        self.assertEqual(self.ll.head.data, 50)
        self.assertNotEqual(self.ll.head, old_head)

    def test_add_in_new_list_adds_a_node_as_tail_and_head(self):
        ll_new = DoublyLinkedList()
        ll_new.add(25)

        self.assertEqual(ll_new.head, ll_new.tail)
    
    def test_peek_first_and_last(self):
        peeked_first = self.ll.peek_first()
        peeked_last = self.ll.peek_last()

        self.assertEqual(peeked_first, self.ll.head)
        self.assertEqual(peeked_last, self.ll.tail)
    
    def test_removing_head(self):
        new_head = self.ll.head.next

        self.ll.remove_at(0)
        
        self.assertEqual(new_head, self.ll.head)
    
    def test_removing_tail(self):
        new_tail = self.ll.tail.prev

        self.ll.remove_at(self.ll.size() - 1)

        self.assertEqual(new_tail, self.ll.tail)
    
    def test_remove_value(self):
        self.assertTrue(self.ll.remove_val(10))
        self.assertFalse(self.ll.remove_val(99))

    def test_contains(self):
        self.assertTrue(self.ll.contains(10))
        self.assertFalse(self.ll.contains(99))
    
    def test_str_reprsentation(self):
        self.assertEqual('[10, 5, 15]', str(self.ll))
