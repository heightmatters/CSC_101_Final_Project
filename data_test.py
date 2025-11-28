import unittest
from data import WaterRecord

class TestWaterRecord(unittest.TestCase):

    def test_WaterRecord_1(self):
        record = WaterRecord(2020, 12.5, 100.0, 85.3, True)

        #check that each value matches approriately. Almost equal catches any rounding errors, although that
        #shouldn't be a problem here as code was written to round accurately.
        self.assertEqual(record.year, 2020)
        self.assertAlmostEqual(record.bawsca, 12.5)
        self.assertAlmostEqual(record.bawsca_total_use, 100.0)
        self.assertAlmostEqual(record.ebmud, 85.3)
        self.assertTrue(record.drought)

        #self.assertIn checks that the specific phrase is within the test. In the case of the first statement,
        #it ensures that the phrase "Year: 2020" is in the text
        text = repr(record)
        self.assertIn("Year: 2020", text)
        self.assertIn("BAWSCA SF RWS Purchases: 12.5", text)
        self.assertIn("Drought: True", text)

    def test_WaterRecord_2(self):
        #Testing an extreme case which is out of your data set/
        record = WaterRecord(1999, 0.0, 0.0, 0.0, False)

        self.assertEqual(record.year, 1999)
        self.assertEqual(record.bawsca, 0.0)
        self.assertEqual(record.bawsca_total_use, 0.0)
        self.assertEqual(record.ebmud, 0.0)
        self.assertFalse(record.drought)

        text = repr(record)
        self.assertIn("Year: 1999", text)
        self.assertIn("BAWSCA SF RWS Purchases: 0.0", text)
        self.assertIn("Drought: False", text)


if __name__ == "__main__":
    unittest.main()
