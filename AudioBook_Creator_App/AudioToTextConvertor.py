#This program will convert a pdf to an audiobook

#Imports
import pyttsx3
import pdfplumber
import PyPDF2

#Get the File name and Location
file = 'One Page.pdf'
print("Done creating a file variable")

#Create a variable to save the book text content
full_text_content = ""
print("Done creating a file variable")

#Create a PDF File Object
pdfFile = open(file, 'rb')
print("Done creating a PDF file object")

#Create a PDF File Reader Object
pdfReader = PyPDF2.PdfFileReader(pdfFile)
print("Done creating a PDF file reader object")

#Get the number of pages
pages = pdfReader.numPages
print("Done getting pages of pdf reader")

#Create a pdfplumber object and loop through the number of pages in PDF file
with pdfplumber.open(file) as pdf:
    #Loop through the number of pages
    print(pdf)
    for i in range(0, pages) :
        print(i)
        page = pdf.pages[i]
        print(page)
        text = page.extract_text()
        print(text)
        speaker = pyttsx3.init()
        speaker.say(text)
        speaker.runAndWait()

