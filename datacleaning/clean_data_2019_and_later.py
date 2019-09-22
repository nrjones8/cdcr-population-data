import tabula

import field_names

from prison_name_mapping import PrisonNames, STANDARDIZED_PRISON_NAMES
from cdcr_util import make_numeric

FOLSOM_UNGENDERED_PRISON_NAME = 'Folsom State Prison (FOL)'
# When we see a row marked "Female Institutions", we've finished processing the data from male
# prisons
START_OF_FEMALE_PRISONS = 'Female Institutions'

def clean_data_from_pdf_2019_and_later(pdf_path, year, month):
    # lol this is literally magic
    tabula_parsed = tabula.read_pdf(pdf_path, pages=[2])
    tabula_parsed.columns = [
        field_names.INSTITUTION_NAME,
        field_names.TOTAL_POPULATION,
        field_names.DESIGNED_CAP,
        field_names.PCT_OCCUPIED,
        field_names.STAFFED_CAP
    ]

    as_dicts = tabula_parsed.to_dict('records')
    # Male population counts show up first, followed by female. For prisons that have the same name
    # in the data, keep track of whether or not we're still processing male section
    processing_male_prisons = True

    population_data = []
    for d in as_dicts:
        institution_name = d[field_names.INSTITUTION_NAME]

        if institution_name == FOLSOM_UNGENDERED_PRISON_NAME:
            institution_name = PrisonNames.FOL_MALE if processing_male_prisons else PrisonNames.FOL_FEMALE

        if institution_name not in STANDARDIZED_PRISON_NAMES:
            print('Skipping row: {}, not a population row'.format(d))
            # When we see a row marked "Female Institutions", we've finished processing the data
            # from male prisons
            if institution_name == 'Female Institutions':
                processing_male_prisons = False

            continue

        # map the name to a normalized one
        normalized_prison_name = STANDARDIZED_PRISON_NAMES[institution_name]

        # The "default" for SQ is male, since only 2019 and later reports have SQ female numbers
        if normalized_prison_name == PrisonNames.SQ:
            normalized_prison_name = PrisonNames.SQ if processing_male_prisons else PrisonNames.SQ_FEMALE

        population_data.append({
            field_names.YEAR: year,
            field_names.MONTH: month,
            field_names.INSTITUTION_NAME: normalized_prison_name,
            # in the newer PDFs, there's no split/distinction between "civil addict" and people
            # with felonies - so total pop == number of people with felonies
            field_names.NUM_PEOPLE_WITH_FELONIES: make_numeric(d[field_names.TOTAL_POPULATION]),
            field_names.NUM_CIVIL_ADDICT: 0,

            field_names.TOTAL_POPULATION: make_numeric(d[field_names.TOTAL_POPULATION]),
            field_names.DESIGNED_CAP: make_numeric(d[field_names.DESIGNED_CAP]),
            field_names.PCT_OCCUPIED: make_numeric(d[field_names.PCT_OCCUPIED]),
            field_names.STAFFED_CAP: make_numeric(d[field_names.STAFFED_CAP]),
            field_names.SOURCE_PDF: pdf_path
        })

    return population_data


if __name__ == '__main__':
    all_data = clean_data_from_pdf_2019_and_later(
        '/Users/nick/src/cdcr-population-data/data/raw_monthly_pdfs/Tpop1d1904.pdf',
        2019,
        4
    )
    for d in all_data:
        print(d)

    print('total num prisons', len(all_data))