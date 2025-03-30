import unittest
import pandas as pd
import sys
import os

# Fix import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from analysis import production_by_region, production_by_well

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        # Controlled test data with repeated well_ids and regions
        self.test_data = pd.DataFrame({
            'well_id': [1, 2, 3, 1, 2],
            'volume_produced': [500, 400, 600, 550, 450],
            'region': ['Texas', 'Oklahoma', 'Texas', 'Texas', 'Oklahoma']
        })

    def test_production_by_region(self):
        region_prod = production_by_region(self.test_data)

        expected = {
            'Texas': 1650,     # 500 + 600 + 550
            'Oklahoma': 850    # 400 + 450
        }

        for region, value in expected.items():
            self.assertEqual(region_prod.get(region), value)

    def test_production_by_well(self):
        well_prod = production_by_well(self.test_data)

        expected = {
            1: 1050,   # 500 + 550
            2: 850,    # 400 + 450
            3: 600     # 600
        }

        for well_id, value in expected.items():
            self.assertEqual(well_prod.get(well_id), value)

if __name__ == '__main__':
    unittest.main()

