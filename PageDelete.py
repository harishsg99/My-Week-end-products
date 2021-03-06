## Code to delete a specific page from a PDF file

from PyPDF2 import PdfFileWriter, PdfFileReader
import sys

filename = sys.argv[1]
number = sys.argv[2]
pages_to_delete = [number] # page numbering starts from 0
infile = PdfFileReader(filename, 'rb')
output = PdfFileWriter()

for i in range(infile.getNumPages()):
    if i not in pages_to_delete:
        p = infile.getPage(i)
        output.addPage(p)

with open(f'new{filename}', 'wb') as f:
    output.write(f)