import re

def get_year_month_from_pdf_name(pdf_name):
    # TPOP1Ad1810.pdf --> example of pre-2019
    # Tpop1d1905.pdf --> example of 2019 and later
    regex_pre_2019 = 'TPOP1Ad(\d{2})(\d{2}).pdf'
    regex_2019_later = 'Tpop1d(\d{2})(\d{2}).pdf'
    m = re.match(regex_pre_2019, pdf_name)

    if m is None:
        m = re.match(regex_2019_later, pdf_name)

    if m is None:
        raise Exception('Could not parse year and month from pdf_name "{}"'.format(pdf_name))

    year = m.group(1)
    if int(year) < 28:
        # Hopefully by 2028, these datasets will not be in PDFs.
        full_year = '20' + year
    else:
        # Anything with a two-digit year greater should be from the 1900s
        full_year = '19' + year

    month = m.group(2)

    return full_year, month

def make_numeric(s):
    without_commas = s.replace(',', '').strip()
    if '.' in without_commas:
        return float(without_commas)
    else:
        return int(without_commas)
