# I tried PyPDF2, pdfminer, pymupdf , tika , PDFium. 


"""
to make below work, I installed Choco, and followed the official documnetation at https://ocrmypdf.readthedocs.io/en/latest/
I have installed ocrmypdf with "pip install ocrmypdf --user"
I have downloaded Polish language pack for the ocrmypdf / tesseract

"""
import ocrmypdf
import os

# Why I define function taking 2 arguments, then make this function take 4 in the example?
# And why do I call it later just by "ocr", not by the full "ocrmypdf.ocr", and it works?
def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, force_ocr=True, l="pol")

print('We are here')
print("We are here with double quotation marks")

# Define path to unreadable .pdfs
path_to_pdfs_input = r"C:\Selenium\Pobieranie/"
path_to_pdfs_output = r"C:\Selenium\Czytelne/"

# Get the file names in the directory
                                            # czy ja muszę łapać za nazwy pliku, nie mogę po prostu wszystkich plików wrzucić do ocrmypdf, i łapać następny kolejny???
counter = 0
for root, dirs, file_names in os.walk(path_to_pdfs_input):
    total_amount_of_files = len(file_names)
    for file_name in file_names:
        ocr(path_to_pdfs_input+file_name, path_to_pdfs_output+file_name)
        counter += 1                                                                         
        print("Przekonwertowany został %d plik na %d plików" %(counter, total_amount_of_files)) 

print("Pomyślnie ukończono zadanie!")



"""
1.point is to do that for next 20 PDFs
    once PDF is readable, either check if ocr my PDF is storing the text in a string that can be called
    if not, open and read the whole document with file reader
    (if that does not work store output file in .txt format)

    Get the data that interest you (name, year, amount of donations received, amount of donations spent on statutory cause)

    Save the file in organisation name - year convention   


"""
