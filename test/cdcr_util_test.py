import unittest

from datacleaning.cdcr_util import get_year_month_from_pdf_name, make_numeric

class CdcrUtilTest(unittest.TestCase):
    def test_parses_pdf_name(self):
        self.assertEquals(('2011', '08'), get_year_month_from_pdf_name('TPOP1Ad1108.pdf'))
        self.assertEquals(('1998', '08'), get_year_month_from_pdf_name('TPOP1Ad9808.pdf'))
        self.assertEquals(('2018', '12'), get_year_month_from_pdf_name('TPOP1Ad1812.pdf'))
        self.assertEquals(('2017', '11'), get_year_month_from_pdf_name('TPOP1Ad1711.pdf'))

    def test_parses_2019_names(self):
        self.assertEquals(('2019', '05'), get_year_month_from_pdf_name('Tpop1d1905.pdf'))
        self.assertEquals(('2019', '07'), get_year_month_from_pdf_name('Tpop1d1907.pdf'))

    def test_converts_numbers(self):
        # Comma ints
        self.assertEqual(make_numeric('1,234'), 1234)
        # Check multiple commas too
        self.assertEqual(make_numeric('1,234,567'), 1234567)
        self.assertEqual(make_numeric('1234'), 1234)

        # Decimals
        self.assertEqual(make_numeric('34.5'), 34.5)
        self.assertEqual(make_numeric('2.3'), 2.3)

if __name__ == '__main__':
    unittest.main()
