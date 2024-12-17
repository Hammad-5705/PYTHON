from PyPDF2 import PdfWriter
import os

merger = PdfWriter()

direc="D:/Cources/PYTHON/garbage"
os.chdir(direc)
files=[file for file in os.listdir(direc) if file.endswith(".pdf")]

for pdf in files:
    merger.append(os.path.join(direc,pdf))

merger.write("merged-pdf.pdf")
merger.close()
print("SUCESSFULLY CREATED")