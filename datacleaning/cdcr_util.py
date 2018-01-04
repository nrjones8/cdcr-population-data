import re

def get_year_month_from_pdf_name(pdf_name):
    m = re.match('TPOP1Ad(\d{2})(\d{2}).pdf', pdf_name)
    year = m.group(1)
    if int(year) < 28:
        # Hopefully by 2028, these datasets will not be in PDFs.
        full_year = '20' + year
    else:
        # Anything with a two-digit year greater should be from the 1900s
        full_year = '19' + year

    month = m.group(2)

    return full_year, month