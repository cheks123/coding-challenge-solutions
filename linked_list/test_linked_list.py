import unittest
from linked_list import LinkedList

class TestEmptyLinkedList(unittest.TestCase):
    def setUp(self):
        self.lkl = LinkedList()
    
    def test_is_empty(self):
        self.assertTrue(self.lkl.is_empty())
    
    def test_get_size(self):
        self.assertEqual(self.lkl.get_size(), 0)
    
    def test_pop_error(self):
        self.assertTrue(self.lkl.pop())



class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        for i in range(10):
            self.ll.push(i)

    def test_is_empty(self):
        self.assertFalse(self.ll.is_empty())

    def test_get_size(self):
        self.assertEqual(self.ll.get_size(), 10)
    
    def test_push(self):
        
        self.assertEqual(self.ll.get_size(), 10)
        self.assertEqual(self.ll.pop(), 9)
        self.assertEqual(self.ll.get_size(), 9)
    
    def test_get_list(self):
        self.assertEqual(list(map(int, self.ll.get_list().split('->'))), [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
