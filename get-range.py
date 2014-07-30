"""get a subrange of pages from a multipage pdf"""

from PyPDF2 import PdfFileReader, PdfFileWriter
from common import check_pdf_filename, append_to_pdf_filename

def parse():
    """handle all of the argument parsing for this script"""
    import argparse
    ap = argparse.ArgumentParser('python get-range.py')
    ap.add_argument('first', type=int, help='the first page number')
    ap.add_argument('last', type=int, help='the last page number')
    ap.add_argument('input', help='the input pdf file')
    return ap.parse_args()

def main(args):
    """run this script"""
    input_pdf = PdfFileReader(file(args.input, 'r'))
    output = PdfFileWriter()
    for page_number in range(args.first, args.last+1):
        output.addPage(input_pdf.getPage(page_number))
    to_append = '_pages%i_%i' % (args.first, args.last)
    outputstream = file(append_to_pdf_filename(to_append, args.input), 'w')
    output.write(outputstream)
    outputstream.close()

if __name__ == '__main__':
    args = parse()
    check_pdf_filename(args.input)
    main(args)
