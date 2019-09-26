from arrays.dynamic_array import DynamicArray
import unittest


class DynamicArrayTest(unittest.TestCase):

    def setUp(self):
        self.arr = DynamicArray(1)

    def test_capacity_on_create(self):
        self.assertEquals(1, self.arr.capacity)

    def test_get_element(self):
        self.arr.add(5)

        self.assertEquals(5, self.arr.get(0))

    def test_set_element(self):
        arr1 = DynamicArray(1)

        arr1.add(100)
        arr1.add(100)

        arr2 = arr1
        arr2.set(0, 10)

        self.assertEquals(arr2.get(0), 10)
        self.assertNotEquals(arr2.get(0), arr1.get(1))

    def test_size(self):
        self.arr.add(5)
        self.arr.add(6)

        self.assertEquals(2, self.arr.size())
    
    def test_clear_array(self):
        self.arr.add(10)
        self.arr.add(5)

        self.arr.clear()

        self.assertEquals(2, self.arr.size())
        self.assertEquals(None, self.arr.get(0))
    def test_add_element(self):
        self.arr.add(1)
        self.arr.add(5)

        self.assertEquals(str(self.arr), '[1,5]')

    def test_add_element_increases_capacity_dynamically(self):
        start_capacity = self.arr.capacity

        self.arr.add(5)
        self.arr.add(6)

        self.assertTrue(self.arr.capacity > start_capacity)

    def test_remove_at(self):
        self.arr.add(5)
        
        self.assertEquals(5, self.arr.remove_at(0))
        self.assertRaises(IndexError, lambda: self.arr.remove_at(0))

    def test_remove(self):
        self.arr.add(50)
        self.arr.add(60)
        self.arr.add(100)

        self.arr.remove(100)
        
        self.assertEquals(-1, self.arr.index_of(100))
        self.assertEquals(str(self.arr), '[50,60]')

    def test_index_of(self):
        self.arr.add(10)

        self.assertEquals(0, self.arr.index_of(10))
    
    def test_contains(self):
        self.arr.add(5)

        self.assertTrue(self.arr.contains(5))
