import unittest

from datacleaning.clean_data import make_numeric, parse_fields_from_single_line

class DataPrepTests(unittest.TestCase):
    def test_converts_a_pdf(self):
        # Use a real PDF, check the number of lines, one specific line
        pass

    def test_converts_numbers(self):
        # Comma ints
        self.assertEqual(make_numeric('1,234'), 1234)
        # Check multiple commas too
        self.assertEqual(make_numeric('1,234,567'), 1234567)
        self.assertEqual(make_numeric('1234'), 1234)

        # Decimals
        self.assertEqual(make_numeric('34.5'), 34.5)
        self.assertEqual(make_numeric('2.3'), 2.3)

    def test_parses_line_with_no_civil_addict(self):
        # Example line taken from this dataset:
        # https://www.cdcr.ca.gov/Reports_Research/Offender_Information_Services_Branch/Monthly/TPOP1A/TPOP1Ad1711.pdf
        # When there is a "0" for the "civil addict" column
        parsed_san_quentin = parse_fields_from_single_line(
            'SQ   (San Quentin SP)                 4,035               4,035     3,082     130.9        3,988',
            'MALE'
        )
        self.assertEquals(parsed_san_quentin, {
            'institution_name': 'SQ (SAN QUENTIN SP)',
            'population_felons': 4035,
            'civil_addict': 0,
            'total_population': 4035,
            'designed_capacity': 3082,
            'percent_occupied': 130.9,
            'staffed_capacity': 3988,
        })


    def test_parses_line_with_non_zero_civil_addict(self):
        # Example from: https://www.cdcr.ca.gov/Reports_Research/Offender_Information_Services_Branch/Monthly/TPOP1A/TPOP1Ad1705.pdf
        parsed_chcf = parse_fields_from_single_line(
            'CHCF (CA Health Care Fac - Stockton)  2,378  1   2,379   2,951   80.6   2,951',
            'MALE'
        )
        self.assertEquals(parsed_chcf, {
            'institution_name': 'CHCF (CA HEALTH CARE FAC - STOCKTON)',
            'population_felons': 2378,
            'civil_addict': 1,
            'total_population': 2379,
            'designed_capacity': 2951,
            'percent_occupied': 80.6,
            'staffed_capacity': 2951,
        })

    def test_includes_gender_for_folsom(self):
        parsed_san_quentin = parse_fields_from_single_line(
            'FOL (Folsom SP)                 4,035               4,035     3,082     130.9        3,988',
            'MALE'
        )
        self.assertEquals(parsed_san_quentin, {
            'institution_name': 'FOL (FOLSOM SP) (MALE)',
            'population_felons': 4035,
            'civil_addict': 0,
            'total_population': 4035,
            'designed_capacity': 3082,
            'percent_occupied': 130.9,
            'staffed_capacity': 3988,
        })

if __name__ == '__main__':
    unittest.main()