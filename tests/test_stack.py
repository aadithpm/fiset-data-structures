from stack.stack import Stack
import unittest

class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(5)
        self.stack.push(10)
    
    def test_push_puts_element_on_top(self):
        self.stack.push(20)
        
        self.assertEqual(20, self.stack.peek())
        
    def test_pop_removes_first_element(self):
        top_elem = self.stack.peek()

        self.assertEqual(self.stack.pop(), top_elem)
    
    def test_cannot_peek_or_pop_empty_stack(self):
        empty_stack = Stack()

        self.assertRaises(RuntimeError, lambda: empty_stack.pop())
        self.assertRaises(RuntimeError, lambda: empty_stack.peek())

    def test_pop_clears_element_and_affects_length_of_stack(self):
        length = self.stack.size()

        self.stack.push(55)
        self.stack.pop()
        
        self.assertEqual(length, self.stack.size())
