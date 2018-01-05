import argparse
import csv
import os

from cdcr_util import get_year_month_from_pdf_name
from clean_data import clean_data_from_pdf

import field_names

def write_csv(dataset, csv_path, column_names):
    """
    dataset - should be a list of dicts, each is a "row"
    csv_path - path to save data to
    column_names - the names of the columns for the CSV, in the desired order of columns in the CSV
    """
    with open(csv_path, 'w') as f:
        writer = csv.DictWriter(f, column_names)
        writer.writeheader()
        for row in dataset:
            writer.writerow(row)

def compare_year_month(row1, row2):
    if int(row1['year']) > int(row2['year']):
        return 1
    elif int(row1['year']) == int(row2['year']) and int(row1['month']) > int(row2['month']):
        return 1

    return -1

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true', help='display progress')
    parser.add_argument(
        '-o',
        '--outfile',
        default='data/monthly_cdcr_population.csv',
        help='Output path for the CSV of parsed data'
    )
    return parser.parse_args()

def main():
    cl_args = get_args()

    combined_data = []
    pdfs_dir_to_process = 'data/raw_monthly_pdfs/'
    for pdf in os.listdir(pdfs_dir_to_process):
        # The month and year of the data are encoded in the PDF's name. Parse them out here.
        year, month = get_year_month_from_pdf_name(pdf)
        full_path = pdfs_dir_to_process + pdf

        if cl_args.verbose:
            print 'Processing {} with year {} and month {}'.format(full_path, year, month)

        if full_path.endswith('.pdf'):
            cleaned_data = clean_data_from_pdf(full_path)

            # Add the month and year here, since they're not included in the data we're parsing out
            # of the PDFs. We could hypothetically do that, but the file-naming convention should
            # work too.
            for i in range(len(cleaned_data)):
                cleaned_data[i][field_names.MONTH] = month
                cleaned_data[i][field_names.YEAR] = year
                cleaned_data[i][field_names.SOURCE_PDF] = pdf

            combined_data.extend(cleaned_data)

    combined_data.sort(cmp=compare_year_month)
    # sort them by year, month
    fields_in_order = [
        field_names.YEAR,
        field_names.MONTH,
        field_names.INSTITUTION_NAME,
        field_names.NUM_PEOPLE_WITH_FELONIES,
        field_names.NUM_CIVIL_ADDICT,
        field_names.TOTAL_POPULATION,
        field_names.DESIGNED_CAP,
        field_names.PCT_OCCUPIED,
        field_names.STAFFED_CAP,
        field_names.SOURCE_PDF
    ]
    write_csv(combined_data, cl_args.outfile, fields_in_order)
    print 'Wrote output to {}'.format(cl_args.outfile)

if __name__ == '__main__':
    main()