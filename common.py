"""functions common to all scripts"""

def is_pdf_filename(filename):
    return filename.endswith('.pdf')

def check_pdf_filename(filename):
    if not is_pdf_filename(filename):
        print 'error, unrecognised filename'
        exit(-1)
    return

def append_to_pdf_filename(to_append, pdf_filename):
    """creates a new filename for output pdf"""
    new_name = pdf_filename.replace('.pdf', '')
    new_name += to_append + '.pdf'
    return new_name


