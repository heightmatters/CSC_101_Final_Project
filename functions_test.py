import data
import functions
import unittest

#initialized list for us to use in our test cases. Please use this when testing if possible.
waterlist=[
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
        result = functions.water_use_average(waterlist,"BAWSCA Total Use",True)
        expected = round((193.38+205.38+197.44+175.60+197.70),2)/5
        self.assertEqual(result,expected)

    def test_water_use_average_2(self):
        result = functions.water_use_average(waterlist,"EBMUD Gross Water Production",False)
        expected = round((151+147+163+166+155),2)/5
        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()