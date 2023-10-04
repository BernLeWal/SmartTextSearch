#!/bin/python
import os
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io


def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    return data



if __name__ == '__main__':
    documents_dir = "./docs"
    dataset_dir = "./dataset"

    files = [f for f in os.listdir("./docs") if f.endswith('.pdf')]
    for i, filename in enumerate(files):
        print( f"Convert file {i}: '{filename}' into plain-text.")

        text = pdfparser(os.path.join(documents_dir, filename))
        #print( text )

        txtfilepath = os.path.join(dataset_dir, filename).replace('.pdf', '.txt')
        with open(txtfilepath, 'w', encoding='utf-8') as f:
            f.write(text)
