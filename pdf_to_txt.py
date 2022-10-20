import ocrmypdf       
import os               

# Sidecar argument is telling the function to produce a .txt file as well
# Not sure if I need both language and l, but let's have them both stay
def ocr(file_path, save_path):
    ocrmypdf.ocr(file_path, save_path, sidecar=path_to_txt_output+file_name[:-3]+"txt",force_ocr=True, language="pol", l="pol", progress_bar=False)

# Define path to unreadable .pdfs
path_to_pdfs_input = r"C:\Selenium\Pobieranie/"

# Define path to the output of .pdfs and .txt
path_to_pdfs_output = r"C:\Selenium\Czytelne/"
path_to_txt_output = r"C:\Selenium\Tekstowe/"

# Get the file names in the directory

counter = 0
for root, dirs, file_names in os.walk(path_to_pdfs_input):
    total_amount_of_files = len(file_names)
    for file_name in file_names:
        ocr(path_to_pdfs_input+file_name, path_to_pdfs_output+file_name)
        counter += 1                                                    
        print("Przekonwertowany został %d plik na %d plików" %(counter, total_amount_of_files))   

print("Pomyślnie ukończono zadanie!")
