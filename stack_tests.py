import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        self.assertTrue(stack.is_empty())
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(), 5)

    def test_pop(self):
        stack = Stack(5)
        stack.push("legen")
        stack.push("DaIrY")
        self.assertEqual(stack.pop(),"DaIrY")

    def test_peek(self):
        stack = Stack(5)
        stack.push("legen")
        stack.push("DaIrY")
        stack.pop()
        self.assertEqual(stack.peek(),"legen")

    def test_push_error(self):
        stack = Stack(1)
        stack.push("food")
        with self.assertRaises(IndexError):
            stack.push("more food")

    def test_pop_error(self):
        stack = Stack(1)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_error(self):
        stack = Stack(1)
        self.assertTrue(stack.is_empty(), True)
        with self.assertRaises(IndexError):
            stack.peek()

    def test_stack0(self):
        stack = Stack(0)
        self.assertTrue(stack.is_empty())
        self.assertTrue(stack.is_full())

if __name__ == '__main__': 
    unittest.main()
