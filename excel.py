#import openpyxl

#workbook = openpyxl.load_workbook('example.xlsx')

#print(type(workbook))
import os

os.getcwd()

import PyPDF2
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages) # returns 19, total number of pages

page = reader.getPage(0)
#print(page.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())


