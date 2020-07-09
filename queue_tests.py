import unittest
#from queue_array import Queue
from queue_linked import Queue

class TestLab3(unittest.TestCase):
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_queue_fill_empty_queue(self):
        n = 5
        q = Queue(n)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 0)
        for step in range(1, n):
            q.enqueue(step)
            self.assertEqual(q.size(), step)
            self.assertFalse(q.is_full())
            self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), n - 1)
        q.enqueue(n)
        self.assertEqual(q.size(), n)
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        for step in range(1, n):
            self.assertEqual(q.size(), n - (step - 1))
            self.assertEqual(q.dequeue(), step)
            self.assertFalse(q.is_full())
            self.assertFalse(q.is_empty())
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.dequeue(), n)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())

    def test_enqueue_empty_full(self):
        q = Queue(0)
        self.assertTrue(q.is_empty())
        self.assertTrue(q.is_full())

    def test_dequeue_error(self):
        q = Queue(0)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_enqueue_error(self):
        q = Queue(1)
        q.enqueue(1)
        with self.assertRaises(IndexError):
            q.enqueue("miss")

    def test_size(self):
        q = Queue(1)
        q.enqueue("fill")
        self.assertEqual(q.size(),1)

    def test_enqueue_dequeue_no_cap(self):
        q = Queue(0)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_cap1(self):
        q = Queue(1)
        self.assertEqual(q.size(), 0)
        self.assertFalse(q.is_full())
        self.assertTrue(q.is_empty())
        q.enqueue(None)
        self.assertEqual(q.size(), 1)
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        with self.assertRaises(IndexError):
            q.enqueue(2)
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.size(), 0)
        self.assertFalse(q.is_full())
        self.assertTrue(q.is_empty())
        with self.assertRaises(IndexError):
            q.dequeue()
        self.assertEqual(q.size(), 0)
        self.assertFalse(q.is_full())
        self.assertTrue(q.is_empty())

    def test_cap2(self):
        q = Queue(2)
        self.assertEqual(q.size(), 0)
        self.assertFalse(q.is_full())
        self.assertTrue(q.is_empty())
        q.enqueue(None)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), None)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        self.assertTrue(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.size(), 0)
        self.assertFalse(q.is_full())
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertEqual(q.size(), 1)
        self.assertFalse(q.is_full())
        self.assertFalse(q.is_empty())
        # print("front", q.front, "back", q.back)
        # print(q.front.item, q.front.next, q.back.item, q.back.next)

    def test_queue_fill_to_cap_dequeue(self):
        n = 10
        q = Queue(n)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        for step in range(1, n + 1):
            q.enqueue(step)
            self.assertFalse(q.is_empty())
            self.assertEqual(q.size(), step)
        self.assertTrue(q.is_full())
        for step in range(1, n + 1):
            self.assertEqual(q.dequeue(), step)
            self.assertFalse(q.is_full())
            self.assertEqual(q.size(), n - step)
        self.assertEqual(q.size(), 0)
        with self.assertRaises(IndexError):
            q.dequeue()
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        for step in range(1, n + 1):
            q.enqueue(step)
            self.assertFalse(q.is_empty())
            self.assertEqual(q.size(), step)
        self.assertTrue(q.is_full())
        with self.assertRaises(IndexError):
            q.enqueue("overfill")
        for step in range(1, n + 1):
            self.assertEqual(q.dequeue(), step)
            self.assertFalse(q.is_full())
            self.assertEqual(q.size(), n - step)
        self.assertEqual(q.size(), 0)
        self.assertTrue(q.is_empty())
        self.assertFalse(q.is_full())
        with self.assertRaises(IndexError):
            q.dequeue()



if __name__ == '__main__': 
    unittest.main()
