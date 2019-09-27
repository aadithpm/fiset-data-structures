from arrays.dynamic_array import DynamicArray
import unittest


class DynamicArrayTest(unittest.TestCase):

    def setUp(self):
        self.arr = DynamicArray(1)

    def test_capacity_on_create(self):
        self.assertEqual(1, self.arr.capacity)

    def test_get_element(self):
        self.arr.add(5)

        self.assertEqual(5, self.arr.get(0))

    def test_set_element(self):
        arr1 = DynamicArray(1)

        arr1.add(100)
        arr1.add(100)

        arr2 = arr1
        arr2.set(0, 10)

        self.assertEqual(arr2.get(0), 10)
        self.assertNotEqual(arr2.get(0), arr1.get(1))

    def test_size(self):
        self.arr.add(5)
        self.arr.add(6)

        self.assertEqual(2, self.arr.size())
    
    def test_clear_array(self):
        self.arr.add(10)
        self.arr.add(5)

        self.arr.clear()

        self.assertEqual(2, self.arr.size())
        self.assertEqual(None, self.arr.get(0))

    def test_add_element(self):
        self.arr.add(1)
        self.arr.add(5)

        self.assertEqual(str(self.arr), '[1,5]')

    def test_add_element_increases_capacity_dynamically(self):
        start_capacity = self.arr.capacity

        self.arr.add(5)
        self.arr.add(6)

        self.assertTrue(self.arr.capacity > start_capacity)

    def test_remove_at(self):
        self.arr.add(5)

        self.assertEqual(5, self.arr.remove_at(0))
        self.assertRaises(IndexError, lambda: self.arr.remove_at(0))

    def test_remove(self):
        self.arr.add(50)
        self.arr.add(60)
        self.arr.add(100)

        self.arr.remove(100)

        self.assertEqual(-1, self.arr.index_of(100))
        self.assertEqual(str(self.arr), '[50,60]')

    def test_index_of(self):
        self.arr.add(10)

        self.assertEqual(0, self.arr.index_of(10))
    
    def test_contains(self):
        self.arr.add(5)

        self.assertTrue(self.arr.contains(5))
