import unittest
import pandas as pd
import numpy as np
import sys
import os

# Fix path to import the module from src/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from data_preprocessing import clean_data

class TestDataPreprocessing(unittest.TestCase):

    def test_clean_data_basic(self):

        # Raw dirty test data
         raw = pd.DataFrame({
            'well_id': [1, 2, 3, 3, 4],
            'production_date': ['2023-01-01', None, 'invalid-date', '2023-01-01', '2023-01-02'],
            'volume_produced': ['500', 'not_a_number', 300, np.nan, 200]
        })
         
         cleaned = clean_data(raw)

         # After cleaning:
         # - Row 1 is dropped due to missing date
         # - Row 2 is dropped due to invalid date
         # - Row 3 amd 0 are duplicates -> one dropped
         # - volume_produced is coerced; 'not_a_number' becomes NaN then filled with 0

         # Test correct row count
         self.assertEqual(len(cleaned), 2)

         # Test production_data is datetime
         self.assertTrue(pd.api.types.is_numeric_dtype(cleaned['production_data']))

         # Test all volume_produced are numeric and non-null
         self.assertTrue(pd.api.types.is_numeric_dtype(cleaned['volume_produced']))
         self.assertFalse(cleaned['volume_produced'].isnull().any())

         # Test that the filled value is 0 where expected
         self.assertIn(0.0, cleaned['volume_produced'].values)

         def test_clean_data_handles_empty(self):
              empty_df = pd.DataFrame(colums=['well_id', 'production_date', 'volume_produced'])
              cleaned = clean_data(empty_df)

              self.assertTrue(cleaned.empty)
              self.assertListequal(list(cleaned.columns), ['well_id', 'production_date', 'volume_produced'])
          
    if __name__ == '__main__':
        unittest.main()
