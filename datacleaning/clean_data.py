# Data come from the monthly archive here: https://www.cdcr.ca.gov/Reports_Research/Offender_Information_Services_Branch/Monthly/Monthly_Tpop1a_Archive.html
# One such file: https://www.cdcr.ca.gov/Reports_Research/Offender_Information_Services_Branch/Monthly/TPOP1A/TPOP1Ad1711.pdf
import re

import field_names

from parse_pdfs import parse_pdf_to_string
from prison_name_mapping import STANDARDIZED_PRISON_NAMES


# A single line looks something like this:
# 'SQ   (San Quentin SP)                 4,035               4,035     3,082     130.9        3,988'
PDF_POPULATION_REGEX_WITH_EXTRA = (
    # Institution name
    '(\D+)'
    # The rest are numeric fields
    '([\d|,|\.|\s]+)'
)

def make_numeric(s):
    without_commas = s.replace(',', '').strip()
    if '.' in without_commas:
        return float(without_commas)
    else:
        return int(without_commas)

def sanity_check_cleaned_data(cleaned_data):
    total_institutions = len(cleaned_data)
    num_overcrowded_institutions = 0
    num_people_in_overcrowded = 0
    total_people = 0
    for d in cleaned_data:
        total_people += d['total_population']
        if d['percent_occupied'] > 137.5:
            num_overcrowded_institutions += 1
            num_people_in_overcrowded += d['total_population']

    print num_overcrowded_institutions, 'institutions out of', total_institutions
    print num_people_in_overcrowded, 'people out of', total_people, num_people_in_overcrowded / float(total_people), '%'

def parse_fields_from_single_line(line, gender_suffix):
    """
    """
    # Institution name is first, then the rest are numeric fields. There may be either 5 or 6
    # numeric fields, see below for further explanation
    m = re.match('(\D+)([\d|,|\.|\s]+)', line)
    if m is None:
        # No match, skip this line
        return None
    if 'total' in m.group(1).lower():
        # There are 3 "total" lines - "MALE TOTAL", "FEMALE TOTAL", "INSTITUTIONS/CAMPS TOTAL"
        # Skip those, we only want data for individual institutions
        return None

    if 'comm based' in m.group(1).lower():
        # The January 1996 report has a row for "Comm Based Facilities", which don't have an
        # associated capacity. Since they only show up in one PDF out of 265 PDFs, just skip those
        # two lines.
        return None

    # Get rid of extra whitespace
    institution_name = re.sub('\s+', ' ', m.group(1)).strip()

    # Different PDFs use different capitalization. E.g. 2008 calls Pelican Bay:
    # "PELICAN BAY SP" while in 2013 it started being called:
    # "Pelican Bay SP" (i.e. not all caps)
    institution_name = institution_name.upper()

    if 'folsom' in institution_name.lower():
        # There is a "FOL (Folsom SP)" prison for both men and women - add the provided gender to
        # distinguish between the two
        institution_name += ' ({})'.format(gender_suffix)

    numeric_fields = m.group(2).split()

    numeric_field_names = [
        field_names.NUM_PEOPLE_WITH_FELONIES,
        field_names.NUM_CIVIL_ADDICT,
        field_names.TOTAL_POPULATION,
        field_names.DESIGNED_CAP,
        field_names.PCT_OCCUPIED,
        field_names.STAFFED_CAP
    ]

    if len(numeric_fields) not in (5, 6):
        # If there are numeric fields for other data, ignore them
        return None
    elif len(numeric_fields) == 5:
        # When there are 0 in the "civic addict" column, the PDF just omits that column altogether.
        # If we have 5 numeric fields, that means the "civil addict" field was omitted. Add a 0
        # for that field (it's the second numeric field, so insert it at index 1).
        # This is confusing, but unit tests do cover it.
        numeric_fields.insert(1, '0')

    as_numeric_types = [make_numeric(x) for x in numeric_fields]
    parsed_fields = dict(zip(numeric_field_names, as_numeric_types))

    # Sometimes the same prison is referred to by different names. Use the standardized map to
    # make sure we're always using the same naming convention
    standardized_name = STANDARDIZED_PRISON_NAMES[institution_name]
    parsed_fields[field_names.INSTITUTION_NAME] = standardized_name

    return parsed_fields

def clean_data_from_pdf(pdf_path):
    # The prison population numbers are on page 2 of the report, but the pages are zero-index. So
    # we'll just process that single page
    pdf_as_string = parse_pdf_to_string(pdf_path, {1})

    cleaned_data = []
    current_gender = 'MALE'
    for line in pdf_as_string.split('\n'):
        if 'MALE TOTAL' in line:
            # The male prisons are listed first; once we hit the "MALE TOTAL" line, then we know
            # that female prisons are next. We need to distinguish between the two because one
            # prison, "FOL (Folsom SP)", has the same name - one for men, one for women. If we
            # don't include the gender in the name of the prison itself, analyzing the data will be
            # a bit messier, since there will be a duplicate entry for Folsom.
            current_gender = 'FEMALE'
        parsed_line = parse_fields_from_single_line(line, current_gender)
        if parsed_line is not None:
            cleaned_data.append(parsed_line)

    return cleaned_data
