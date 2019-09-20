import unittest
import get_column_stats as gcs

class TestGetColumnStats(unittest.TestCase):

    # test to make sure list is not empty
    def test_list_mean_empty_list(self):
        r = gcs.mean([])
        self.assertEqual(r, None)
                             
    # self assertion test with one value
    def test_list_mean_const_small(self):
        r = gcs.mean([1])
        self.assertEqual(r, 1)
    

    def test_list_mean_list_not_passed(self):
                             
        with self.assertRaises(TypeError) as ex:
            r = gcs.mean('not a list')
            self.assertEqual(str(ex.exception), 'Mean undefined')
        
    # test to make sure list is not empty
    def test_list_stdev_empty_list(self):
        r = gcs.stdev([])
        self.assertEqual(r, None)
    
    # self assertion test with one value
    def test_list_stdev_const_small(self):
        r = gcs.stdev([1])
        self.assertEqual(r, 0)

    def test_list_stdev_list_not_passed(self):
                             
        with self.assertRaises(TypeError) as ex:
            r = gcs.stdev('not a list')
            self.assertEqual(str(ex.exception), 'Stdev undefined')   
    
if __name__ == '__main__':
    unittest.main()
                             
  
                             
        
  

