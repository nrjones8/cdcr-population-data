import os
import requests
import time

PDF_PATH_FORMAT = 'TPOP1Ad{two_digit_year}{zero_padded_month}.pdf'

MONTHLY_BASE_URL = (
    'https://www.cdcr.ca.gov/Reports_Research/Offender_Information_Services_Branch/'
    'Monthly/TPOP1A/{}'.format(PDF_PATH_FORMAT)
)

# 1996 appears to be the first year that this particular format was used.
# Also, there are better ways to do this.
TWO_DIGIT_YEARS = [str(x) for x in range(96, 100)] + [
    '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13',
    '14', '15', '16', '17', '18', '19'
]

TWO_DIGIT_MONTHS = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

def generate_monthly_urls():
    # Just hard-code since 2010 - can get earlier data as well, later on.
    all_urls = []
    for year in TWO_DIGIT_YEARS:
        for month in TWO_DIGIT_MONTHS:
            all_urls.append(MONTHLY_BASE_URL.format(
                two_digit_year=year, zero_padded_month=month
            ))
    return all_urls

def download_monthly_report_pdf(url, pdf_save_path):
    """
    url - the url to download PDF from
    pdf_save_path - the path to save the downloaded PDF to
    """

    response = requests.get(url, stream=True)
    if response.status_code != 200:
        print 'Non-200 from {}, got a {}. Moving on to the next one...'.format(
            url, response.status_code
        )
        return

    with open(pdf_save_path, 'wb') as f:
        f.write(response.content)
    print 'Downloaded {} to {}'.format(url, pdf_save_path)

def download_for_all_year_months():
    monthly_urls = generate_monthly_urls()
    for url in monthly_urls:
        pdf_name = url.split('/')[-1]
        pdf_path = 'data/raw_monthly_pdfs/{}'.format(pdf_name)

        # TODO - add a flag to re-download old PDFs too
        if os.path.isfile(pdf_path):
            print 'Skipping {} because it already exists'.format(pdf_path)
            continue

        download_monthly_report_pdf(url, pdf_path)
        time.sleep(2)

def main():
    download_for_all_year_months()

if __name__ == '__main__':
    main()