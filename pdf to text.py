  
from fpdf import FPDF
import sys
file = sys.argv[1] 
pdf = FPDF()    
pdf.add_page() 
   
pdf.set_font("Arial", size = 15) 
  
f = open(file, "r") 
   
for x in f: 
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C') 
    
pdf.output("output.pdf")    