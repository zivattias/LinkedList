import unittest
from linkedlist import Node, LinkedList


class TestNodeMethods(unittest.TestCase):
    def setUp(self):
        self.node1 = Node(5)
        self.node2 = Node("Hi")
        self.node3 = Node(True)
        self.node4 = Node({"LinkedList": {"Value": False}, 1.5: [1, 2, 3]})

        self.fullnode1 = Node([7, None], self.node3, self.node2)
        self.fullnode2 = Node([], previous_node=self.node2)
        self.fullnode3 = Node("", next_node=self.node1)

    # Node initialization without previous/next nodes
    def test_simple_init(self):
        self.assertEqual(self.node1.value, 5)
        self.node1.value = 4
        self.assertEqual(self.node1.value, 4)
        self.assertEqual(self.node2.value, "Hi")
        self.assertEqual(self.node3.value, True)
        self.assertEqual(
            self.node4.value, {"LinkedList": {"Value": False}, 1.5: [1, 2, 3]}
        )

    # Node initialization with previous/next nodes
    def test_full_init(self):
        self.assertEqual(self.fullnode1.next.value, True)
        self.assertEqual(self.fullnode2.previous, self.node2)
        self.assertEqual(self.fullnode3.value, "")


class TestLinkedListMethods(unittest.TestCase):
    def setUp(self):
        self.linkedlist1 = LinkedList()
        self.linkedlist2 = LinkedList([1, "Hi", True, {1: None}])
        self.linkedlist3 = LinkedList([0, 1, 2, 3, 4])

    # LinkedList lengths
    def test_len(self):
        self.assertEqual(self.linkedlist1.len, len(self.linkedlist1))
        self.assertEqual(len(self.linkedlist2), 4)

    # LinkedList nodes indexing and values, per each LinkedList initialization case
    def test_indexes_and_values(self):
        self.assertIsInstance(self.linkedlist2.head, Node)
        self.assertIsNone(self.linkedlist1.head)
        self.assertIsNone(self.linkedlist1.tail)
        self.assertEqual(self.linkedlist2.head.value, 1)
        self.assertEqual(self.linkedlist2.tail.value, {1: None})
        self.assertEqual(self.linkedlist2.head.next.value, "Hi")

        for _ in range(3):
            value = next(self.linkedlist2)
        self.assertEqual(value, True)

    # Append method, testing LinkedList head & tail instances and values and .next, .previous functionality
    def test_append(self):
        self.linkedlist1.append(1)
        self.assertEqual(self.linkedlist1.head.value, 1)
        self.assertEqual(self.linkedlist1.tail.value, 1)
        self.assertIsInstance(self.linkedlist1.head, Node)
        node = Node(None)
        self.linkedlist1.append(node)
        self.assertEqual(self.linkedlist1.head.next.value, None)
        self.assertEqual(self.linkedlist1.tail.value, None)
        self.assertIsInstance(self.linkedlist1.head.next, Node)
        self.assertEqual(self.linkedlist1.head.next, node)
        self.assertEqual(self.linkedlist1.tail.previous.value, 1)

    # Insertion method, testing exception raisal, correct insertion and post-insertion index adjustment
    def test_insert(self):
        self.assertRaises(IndexError, self.linkedlist1.insert, True, 1)
        self.assertRaises(IndexError, self.linkedlist1.insert, True, -1)
        self.assertRaises(IndexError, self.linkedlist2.insert, True, 5)

        self.linkedlist1.append("Hello")
        self.linkedlist1.append("World")
        sample = Node([{True: {None: ["G", 24.5, {False: [None, 1 * 2]}]}}])
        self.linkedlist1.insert(sample, 1)

        self.assertEqual(self.linkedlist1.head.next.value, sample.value)
        self.assertEqual(self.linkedlist1.head.next, sample)
        self.assertEqual(self.linkedlist1.tail.previous, sample)
        self.assertEqual(len(self.linkedlist1), 3)

    # Removal method, testing exception raisal, correct removal and post-removal index adjustment
    def test_remove(self):
        self.linkedlist3.remove(2)
        self.assertEqual(self.linkedlist3.head.next.next.value, 3)
        self.assertEqual(self.linkedlist3.head.next.next.previous.value, 1)
        self.assertRaises(IndexError, self.linkedlist3.remove, -1)
        self.assertRaises(IndexError, self.linkedlist3.remove, 10)
        self.linkedlist3.remove(3)
        self.assertEqual(self.linkedlist3.tail.value, 3)

    # Contact 2 LinkedLists together, testing length, values and indexes
    def test_contact(self):
        l1 = LinkedList([1, 2, 3])
        l2 = LinkedList([4, 5, 6])
        l3 = l1 + l2
        self.assertEqual(len(l3), len(l1) + len(l2))
        self.assertEqual(l3.tail.value, l2.tail.value)
        self.assertEqual(l3.head.value, l1.head.value)
        self.assertEqual(l3.head.next.next.next.value, l2.head.value)


if __name__ == "__main__":
    unittest.main(verbosity=2)
