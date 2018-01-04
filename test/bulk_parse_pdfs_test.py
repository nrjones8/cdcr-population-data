import unittest

from datacleaning.bulk_parse_pdfs import compare_year_month

class BulkParsePdfsTest(unittest.TestCase):
    def test_sorts_by_date(self):
        self.assertEquals(1, compare_year_month(
            {'year': '2011', 'month': '04'},
            {'year': '2011', 'month': '03'}
        ))
        self.assertEquals(1, compare_year_month(
            {'year': '2014', 'month': '04'},
            {'year': '2011', 'month': '04'}
        ))

        self.assertEquals(-1, compare_year_month(
            {'year': '2011', 'month': '03'},
            {'year': '2011', 'month': '04'}
        ))
        self.assertEquals(-1, compare_year_month(
            {'year': '1999', 'month': '05'},
            {'year': '2011', 'month': '04'}
        ))

if __name__ == '__main__':
    unittest.main()