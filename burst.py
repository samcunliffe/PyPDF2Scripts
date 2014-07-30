"""get all pages from a multipage pdf"""

from PyPDF2 import PdfFileReader, PdfFileWriter
from common import check_pdf_filename, append_to_pdf_filename

def parse():
    """handle all of the argument parsing for this script"""
    import argparse
    ap = argparse.ArgumentParser('python burst.py')
    ap.add_argument('input', help='the input pdf file')
    return ap.parse_args()

def main(args):
    """run this script"""
    input_pdf = PdfFileReader(file(args.input, 'r'))
    for page_number, page in enumerate(input_pdf.pages):
        output = PdfFileWriter()
        output.addPage(page)
        to_append = '_page%i' % page_number
        outputstream = file(append_to_pdf_filename(to_append, args.input), 'w')
        output.write(outputstream)
        outputstream.close()
    return

if __name__ == '__main__':
    args = parse()
    print args
    check_pdf_filename(args.input)
    main(args)
