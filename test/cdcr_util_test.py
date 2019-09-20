import unittest

from datacleaning.cdcr_util import get_year_month_from_pdf_name

class CdcrUtilTest(unittest.TestCase):
    def test_parses_pdf_name(self):
        self.assertEquals(('2011', '08'), get_year_month_from_pdf_name('TPOP1Ad1108.pdf'))
        self.assertEquals(('1998', '08'), get_year_month_from_pdf_name('TPOP1Ad9808.pdf'))
        self.assertEquals(('2018', '12'), get_year_month_from_pdf_name('TPOP1Ad1812.pdf'))
        self.assertEquals(('2017', '11'), get_year_month_from_pdf_name('TPOP1Ad1711.pdf'))

    def test_parses_2019_names(self):
        self.assertEquals(('2019', '05'), get_year_month_from_pdf_name('Tpop1d1905.pdf'))
        self.assertEquals(('2019', '07'), get_year_month_from_pdf_name('Tpop1d1907.pdf'))

if __name__ == '__main__':
    unittest.main()
