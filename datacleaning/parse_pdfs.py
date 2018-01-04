# Help from: http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php
# and https://gist.github.com/jmcarp/7105045
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt

def parse_pdf_to_string(fname, pagenums=None):
    """
    pagenums - a set of zero-indexed pages to process
    """
    if pagenums is None:
        pagenums = set()

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text
