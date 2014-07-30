"""get a single (or range of) page(s) from a multipage pdf"""

from PyPDF2 import PdfFileReader, PdfFileWriter
from common import check_pdf_filename, append_to_pdf_filename

def parse():
    """handle all of the argument parsing for this script"""
    import argparse
    ap = argparse.ArgumentParser('python get-page.py')
    ap.add_argument('page', type=int, help='the page number')
    ap.add_argument('input', help='the input pdf file')
    return ap.parse_args()

def main(args):
    """run this script"""
    input_pdf = PdfFileReader(file(args.input, 'r'))
    output = PdfFileWriter()
    #print "document1.pdf has %d pages." % input1.getNumPages()
    output.addPage(input_pdf.getPage(args.page))
    to_append = '_page%i' % args.page
    outputstream = file(append_to_pdf_filename(to_append, args.input), 'w')
    output.write(outputstream)
    outputstream.close()

if __name__ == '__main__':
    args = parse()
    print args
    check_pdf_filename(args.input)
    main(args)
