from PyPDF2 import PdfFileMerger
import sys
firstpdf = sys.argv[1]
secondpdf = sys.argv[2]

pdfs = [firstpdf,secondpdf]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()