import ocrmypdf       
import os 
import shutil            
from concurrent.futures import ThreadPoolExecutor
import time as t

# https://github.com/tesseract-ocr/tesseract/issues/1799

# ocrmypdf shutsdown after 48 hours?
# python jak zrobić procenty?

### by nie generować .pdf, mogę użyć output-type=none
# Sidecar argument is telling the function to produce a .txt file as well
# Not sure if I need both language and l, but let's have them both stay
# You need to setup folders first

def ocr(file_path, save_path, path_to_txt_output, file_name):
    ocrmypdf.ocr(file_path, save_path, sidecar=path_to_txt_output+file_name[:-3]+"txt", force_ocr=True, language="pol", l="pol", progress_bar=True, output_type="pdf")

def main():
    # Define path to unreadable .pdfs
    path_to_pdfs_input = r"C:\Selenium\Pobieranie/"

    # Define path to the output of .pdfs and .txt
    path_to_pdfs_output = r"C:\Selenium\Czytelne/"
    path_to_txt_output = r"C:\Selenium\Tekstowe/"

    # Get the funciton variables names in the directory
    counter = 0
    time_total = 0
    
    # Start looping through the documents
    for root, dirs, file_names in os.walk(path_to_pdfs_input):
        total_amount_of_files = len(file_names)
        for file_name in file_names:
            t_start = t.time()
            ocr(path_to_pdfs_input+file_name, path_to_pdfs_output+file_name, path_to_txt_output, file_name)
            t_end = t.time()
            time_total += t_end - t_start
            counter += 1                                                    
            print("Przekonwertowany został %d plik na %d plików. To już %d procent!" %(counter, total_amount_of_files, counter/total_amount_of_files))
            if counter % 50 == 0:                                                   #zmieniłem na co 10 bo na co 50 się zbyt długo czeka wg. mnie. To zawsze mogę zmienić na nowo
                with open("czasomierz_dla_konwersji.txt", "a") as file:
                    file.writelines(str(time_total))
                    file.writelines(("\n"))
                    time_total = 0
                shutil.rmtree(path_to_pdfs_output)              # I would like to remove the not used .pdf files
                os.mkdir(path_to_pdfs_output)                   # and I need to create a new folder too

    print("Pomyślnie ukończono zadanie!")

main()
