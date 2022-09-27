# I tried PyPDF2, pdfminer, pymupdf , tika , PDFium. 


"""
to make below work, I installed Chocolatey, and followed the official documnetation at https://ocrmypdf.readthedocs.io/en/latest/
I have installed ocrmypdf with "pip install ocrmypdf --user"
I have downloaded Polish language pack for the ocrmypdf / tesseract

"""
import ocrmypdf

def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, force_ocr=True, l="pol")

print('We are here')
ocr(r"path_to_your_input_file", r"path_to_your_output_file") # no worries, your output will be created for you, just give it a path and a name


"""
1.point is to do that for next 20 PDFs 
    once PDF is readable, either check if ocr my PDF is storing the text in a string that can be called
    if not, open and read the whole document with file reader
    (if that does not work store output file in .txt format)

    Get the data that interest you (name, year, amount of donations received, amount of donations spent on statutory cause)

    Save the file in organisation name - year convention   


"""
