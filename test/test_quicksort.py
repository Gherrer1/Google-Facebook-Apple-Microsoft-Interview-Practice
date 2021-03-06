import unittest
from sort.quicksort import quicksort

class TestQuicksort(unittest.TestCase):
    def test_emptyarr(self):
        arr = []
        quicksort(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, sorted(arr), 'Arrays werent equal')
    
    def test_single_elem_arr(self):
        arr = [4]
        quicksort(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, [4])
        
    def test_double_elem_arr(self):
        arr = [9, 5]
        quicksort(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, [5, 9])

    def test_works_on_odd_len_arr(self):
        arr = [100, 7, 3, 25, 60, 355, 24, 1, 56, 12, 3, 500, 9134, 91, 211]
        quicksort(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, sorted(arr))

    def test_works_on_even_len_arr(self):
        arr = [100, 7, 3, 25, 60, 45, 355, 24, 1, 56, 12, 3, 500, 9134, 91, 211]
        quicksort(arr, 0, len(arr) - 1)
        self.assertListEqual(arr, sorted(arr))