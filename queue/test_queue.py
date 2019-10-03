from .queue import Queue
import unittest


class QueueTest(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(5)
        self.queue.enqueue(10)
        self.queue.enqueue(15)

    def test_enqueue_puts_element_at_the_end(self):
        self.queue.enqueue(25)

        self.assertEqual(25, self.queue.last())

    def test_dequeue_removes_first_inserted_element(self):
        top_elem = self.queue.peek()

        self.assertEqual(self.queue.dequeue(), top_elem)

    def test_cannot_deq_peek_empty_queue(self):
        empty_queue = Queue()

        self.assertRaises(RuntimeError, lambda: empty_queue.dequeue())
        self.assertRaises(RuntimeError, lambda: empty_queue.peek())

    def test_dequeue_changes_length(self):
        length = self.queue.size() - 2

        self.queue.dequeue()
        self.queue.dequeue()

        self.assertEqual(length, self.queue.size())
