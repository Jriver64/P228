import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_implement_basic(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())

    def test_implement_basic_add(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertFalse(t_list.add(15))
        # print(t_list.head.item)
        # i0 = t_list.head.next
        # print(i0.item)
        # i1 = t_list.head.next.next
        # print(i1.item)
        # i2 = t_list.head.next.next.next
        # print(i2.item)

    def test_implement_basic_remove(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertTrue(t_list.remove(15))
        self.assertFalse(t_list.remove(15))
        self.assertTrue(t_list.remove(20))
        # print(t_list.head.prev.item)
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.is_empty())

    def test_implement_basic_index(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertTrue(t_list.remove(15))
        self.assertFalse(t_list.remove(15))
        self.assertTrue(t_list.remove(20))
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(20), 2)
        self.assertEqual(t_list.index(40), None)

    def test_implement_basic_pop(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertTrue(t_list.remove(15))
        self.assertFalse(t_list.remove(15))
        self.assertTrue(t_list.remove(20))
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertFalse(t_list.is_empty())
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(20), 2)
        self.assertEqual(t_list.index(40), None)
        self.assertEqual(t_list.pop(1), 15)
        self.assertEqual(t_list.pop(1), 20)
        self.assertEqual(t_list.pop(0), 10)
        self.assertTrue(t_list.is_empty())
        with self.assertRaises(IndexError):
            print(t_list.pop(0))

    def test_implement_basic_pop_error_greater_size(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(20), 2)
        self.assertEqual(t_list.index(40), None)
        self.assertEqual(t_list.pop(1), 15)
        with self.assertRaises(IndexError):
            print(t_list.pop(2))

    def test_implement_basic_pop_error_neg_index(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(20), 2)
        self.assertEqual(t_list.index(40), None)
        self.assertEqual(t_list.pop(1), 15)
        with self.assertRaises(IndexError):
            print(t_list.pop(-2))

    def test_implement_basic_rec_search(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(20), 2)
        self.assertEqual(t_list.index(40), None)
        self.assertTrue(t_list.search(20))
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(15))
        self.assertFalse(t_list.search(25))

    def test_implement_basic_make_list_and_rev(self):
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        self.assertTrue(t_list.add(10))
        self.assertTrue(t_list.add(20))
        self.assertTrue(t_list.add(15))
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(15), 1)
        self.assertEqual(t_list.index(20), 2)
        self.assertEqual(t_list.index(40), None)
        self.assertTrue(t_list.search(20))
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(15))
        self.assertFalse(t_list.search(25))
        self.assertEqual(t_list.python_list(), [10, 15, 20])
        # print(t_list.head.next.item)
        # print(t_list.head.next.next.item)
        # print(t_list.head.next.next.next.item)
        # print(t_list.head.prev.item)
        # print(t_list.head.prev.prev.item)
        self.assertTrue(t_list.search(15))
        # self.assertEqual(t_list.python_list_reversed(), [20, 15, 10])

    def test_revers_rec(self):
        l = OrderedList()
        self.assertTrue(l.add(10))
        self.assertTrue(l.add(20))
        self.assertTrue(l.add(15))
        # print(l.head.next.item)
        # print(l.head.next.next.item)
        # print(l.head.next.next.next.item)
        # print(l.head.prev.item)
        # print(l.head.prev.prev.item)
        # print(l.head.prev.prev.prev.item)
        self.assertEqual(l.python_list_reversed(), [20, 15, 10])
        self.assertTrue(l.add(12))
        self.assertTrue(l.add(18))
        self.assertTrue(l.add(21))
        self.assertEqual(l.python_list_reversed(), [21, 20, 18, 15, 12, 10])
        self.assertEqual(l.python_list(), [10, 12, 15, 18, 20, 21])

    def test_loop(self):
        n = 5
        varlist = OrderedList()
        self.assertTrue(varlist.is_empty())
        self.assertEqual(varlist.size(), 0)
        self.assertEqual(varlist.python_list(), [])
        self.assertEqual(varlist.python_list_reversed(), [])
        self.assertFalse(varlist.search("My grandma in law just died"))
        self.assertFalse(varlist.remove("And I miss my friends... like a lot"))
        self.assertEqual(varlist.index("And I'm feeling pretty sad"), None)
        with self.assertRaises(IndexError):
            varlist.pop(0)
        with self.assertRaises(IndexError):
            varlist.pop(-1)
        complist = []
        # add sequence
        for val in range(n):
            self.assertTrue(varlist.add(val))
            self.assertFalse(varlist.is_empty())
            self.assertEqual(varlist.size(), val + 1)
            complist += [val]
            self.assertEqual(varlist.python_list(), complist)
            revcomp = complist[::-1]
            self.assertEqual(varlist.python_list_reversed(), revcomp)
            self.assertTrue(varlist.search(val))
            self.assertEqual(varlist.index(val), val)
        # remove sequence (leaves 1 value in list)
        for val in range(n - 1, 0, -1):
            self.assertTrue(varlist.remove(val))
            self.assertFalse(varlist.is_empty())
            self.assertEqual(varlist.size(), val)
            complist = complist[:len(complist) - 1]
            self.assertEqual(varlist.python_list(), complist)
            revcomp = complist[::-1]
            self.assertEqual(varlist.python_list_reversed(), revcomp)
            self.assertFalse(varlist.search(val))
            self.assertEqual(varlist.index(val), None)
        self.assertTrue(varlist.remove(0))
        self.assertTrue(varlist.is_empty())
        complist = []
        self.assertEqual(varlist.python_list(), complist)
        revcomp = complist[::-1]
        self.assertEqual(varlist.python_list(), revcomp)
        # list is now empty
        # add sequence
        for val in range(n):
            self.assertTrue(varlist.add(val))
            self.assertFalse(varlist.is_empty())
            self.assertEqual(varlist.size(), val + 1)
            complist += [val]
            self.assertEqual(varlist.python_list(), complist)
            revcomp = complist[::-1]
            self.assertEqual(varlist.python_list_reversed(), revcomp)
            self.assertTrue(varlist.search(val))
            self.assertEqual(varlist.index(val), val)
        # pop sequence (leaves 1 value in list)
        for val in range(n - 1, 0, -1):
            self.assertEqual(varlist.pop(val), val)
            self.assertFalse(varlist.is_empty())
            self.assertEqual(varlist.size(), val)
            complist = complist[:len(complist) - 1]
            self.assertEqual(varlist.python_list(), complist)
            revcomp = complist[::-1]
            self.assertEqual(varlist.python_list_reversed(), revcomp)
            self.assertFalse(varlist.search(val))
            self.assertEqual(varlist.index(val), None)
        self.assertEqual(varlist.pop(0), 0)
        self.assertTrue(varlist.is_empty())
        # list is now empty
        self.assertEqual(varlist.size(), 0)
        self.assertEqual(varlist.python_list(), [])
        self.assertEqual(varlist.python_list_reversed(), [])
        self.assertFalse(varlist.search("If your're reading this, I hope ur doing well"))
        self.assertFalse(varlist.remove("sorry just decided to vent in my test cases bc can't rlly talk to anyone"))
        self.assertEqual(varlist.index("Do I get 100% on the first try, hope so"), None)
        with self.assertRaises(IndexError):
            varlist.pop(0)
        with self.assertRaises(IndexError):
            varlist.pop(-1)

    def test_strings(self):
        varlist = OrderedList()
        self.assertTrue(varlist.is_empty())
        self.assertTrue(varlist.add("cba"))
        self.assertTrue(varlist.add("bac"))
        self.assertTrue(varlist.add("abc"))
        self.assertFalse(varlist.add("abc"))
        self.assertEqual(varlist.python_list_reversed(), ["cba", "bac", "abc"])
        self.assertEqual(varlist.python_list(), ["abc", "bac", "cba"])
        for val in range(3, 0, -1):
            varlist.pop(val - 1)
        self.assertTrue(varlist.is_empty())
        self.assertEqual(varlist.size(), 0)

    def test_floats(self):
        varlist = OrderedList()
        self.assertTrue(varlist.is_empty())
        self.assertTrue(varlist.add(1.000))
        self.assertTrue(varlist.add(1.050))
        self.assertTrue(varlist.add(.950))
        self.assertFalse(varlist.add(.950))
        self.assertEqual(varlist.python_list_reversed(), [1.050, 1.000, .950])
        self.assertEqual(varlist.python_list(), [.950, 1.000, 1.050])
        for val in range(3, 0, -1):
            varlist.pop(val - 1)
        self.assertTrue(varlist.is_empty())
        self.assertEqual(varlist.size(), 0)


if __name__ == '__main__': 
    unittest.main()
