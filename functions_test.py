import data
import functions
import unittest

# initialized list for us to use in our test cases. Please use this when testing if possible.
waterlist = [
    data.WaterRecord(2024, 123.63, 184.77, 151, False),
    data.WaterRecord(2023, 117.91, 176.64, 147, False),
    data.WaterRecord(2022, 128.11, 193.38, 156, True),
    data.WaterRecord(2021, 134.42, 205.38, 169, True),
    data.WaterRecord(2020, 132.22, 197.44, 167, True),
    data.WaterRecord(2019, 126.00, 195.90, 163, False),
    data.WaterRecord(2018, 128.10, 200.30, 166, False),
    data.WaterRecord(2017, 116.39, 184.78, 155, False),
    data.WaterRecord(2016, 113.20, 175.60, 145, True),
    data.WaterRecord(2015, 126.50, 197.70, 156, True)
]


class TestCases(unittest.TestCase):

    def test_water_use_average_1(self):
        result = functions.water_use_average(waterlist, "BAWSCA Total Use", True)
        expected = round((193.38 + 205.38 + 197.44 + 175.60 + 197.70), 2) / 5
        self.assertEqual(result, expected)

    def test_water_use_average_2(self):
        result = functions.water_use_average(waterlist, "EBMUD Gross Water Production", False)
        expected = round((151 + 147 + 163 + 166 + 155), 2) / 5
        self.assertEqual(result, expected)

    def test_percent_change_bawsca_total_use_1(self):
        changes = functions.percent_change(waterlist, "BAWSCA Total Use")
        first_pair = None
        last_pair = None
        for c in changes:
            if first_pair is None or c[0] < first_pair[0]:
                first_pair = c
            if last_pair is None or c[0] > last_pair[0]:
                last_pair = c
        self.assertEqual(first_pair[0], 2015)
        self.assertEqual(first_pair[1], 2016)
        self.assertAlmostEqual(first_pair[2], -11.18, places=2)
        self.assertEqual(last_pair[0], 2023)
        self.assertEqual(last_pair[1], 2024)
        self.assertAlmostEqual(last_pair[2], 4.6, places=1)

    def test_percent_change_bawsca_total_use_2(self):
        changes = functions.percent_change(waterlist, "BAWSCA Total Use")
        target_pair = None
        for c in changes:
            if c[0] == 2018 and c[1] == 2019:
                target_pair = c
                break
        self.assertIsNotNone(target_pair)
        self.assertAlmostEqual(target_pair[2], -2.20, places=2)

    def test_compare_water_use_bawsca_total_use_1(self):
        pct = functions.compare_water_use(waterlist, "BAWSCA Total Use")
        self.assertAlmostEqual(pct, 2.88, places=2)

    def test_compare_water_use_bawsca_total_use_2(self):
        pct = functions.compare_water_use(waterlist, "BAWSCA Total Use")
        self.assertTrue(pct > 0)
        self.assertAlmostEqual(pct, 2.88, places=2)


if __name__ == '__main__':
    unittest.main()