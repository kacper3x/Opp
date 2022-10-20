import os
import csv

# Creating a list that will store the interesting values for every non profit organization
collection_of_nonprofit_names = []

# Iterating through the directory with the text files for every text file
path_to_directory = "C:\\Selenium\\Tekstowe\\"
for input_filename in os.listdir(path_to_directory):

    # Opening a file, and creating a list permanently append every line to the file
    with open(path_to_directory+input_filename, "r", errors="ignore", encoding="utf8") as f:
        billy = ""
        for x in f:
            billy = "".join(f)    

        # Year of the statement
        year_of_the_statement = ""
        string_with_year_of_nonprofit = billy[: billy.find('2. Adres siedziby')]
        x = string_with_year_of_nonprofit.split()
        for i in x:
            if i.isnumeric() and len(i) == 4:
                year_of_the_statement = i
                break
            # sometimes ORC reads the 2020 as 20 ... 20 into the text file
            elif i.isnumeric() and len(i) == 2:     
                year_of_the_statement += i
            
        # Name of the nonprofit
        name_of_nonprofit = ""
        string_with_name_of_nonprofit = billy[: billy.find('2. Adres siedziby')]
        x = string_with_name_of_nonprofit.split()
        # Gather the capital names with exceptions "I." and "X;" that are in the text, but are not part of the nonprofit name
        # All parts of nonprofit names are capital
        for i in range(len(x)):
            if x[i].isupper() and (x[i] != "I." and x[i] != "X;"):
                name_of_nonprofit += x[i] + " " 
            # I want to add a number to the name of the nonprofit, if the original name contained the name
            # But I do not want the number on front, nonono - then I would be adding numbers to the nonprofit name that weren't there in the first place
            elif x[i].isnumeric() and x[i-1].isupper() and i != 0:
                name_of_nonprofit += x[i] + " "  
        # If OCR could not get the name of the non profit, I get the KRS number
        # I need to add something before the KRS number, otherwise Excel will eat the trailing zeros
        if name_of_nonprofit == "":
            string_with_name_of_nonprofit = billy[: billy.find('8. Skład organu kontroli')]                
            x = string_with_name_of_nonprofit.split()
            for i in x:
                if i.isnumeric() and len(i) == 10:
                    name_of_nonprofit = "KRS   " + i
        # I want to remove the quotation marks encapsulating the name of the nonprofit
        # I want to remove the quotation marks in the whole name of the nonprofit too, if the name starts with the quotation marks
        if name_of_nonprofit[0].isalpha() == False:
            name_of_nonprofit = name_of_nonprofit.replace('"','')

        # Yearly income of the nonprofit
        income_yearly_with_decimal = ""
        string_with_income_of_nonprofit = billy[billy.find('Łączna kwota przychodów organizacji ogółem'): billy.find('Łączna kwota przychodów organizacji ogółem')+1000]
        x = string_with_income_of_nonprofit.split()
        for i in range(len(x)):
            if x[i] == "zł":
                string_with_income_of_nonprofit = x[i-3:i]
                for j in string_with_income_of_nonprofit:
                    if j[0].isnumeric():
                        income_yearly_with_decimal += j
                # Remove last three chars of the salaries yearly
                # We remove the decimal part and "," or "." sing
                # And we cast the string as an integer
                income_yearly = int(income_yearly_with_decimal[:-3])
                break

        # Yearly salaries of the nonprofit
        salaries_yearly_with_decimal = ""
        salaries_yearly = ""
        string_with_salaries_of_nonprofit = billy[billy.find('1.Łączna kwota wynagrodzeń (brutto) wypłaconych'): billy.find('1.Łączna kwota wynagrodzeń (brutto) wypłaconych')+1000]
        x = string_with_salaries_of_nonprofit.split()
        for i in range(len(x)):
            if x[i] == "zł":
                string_with_salaries_of_nonprofit = x[i-3:i]
                for j in string_with_salaries_of_nonprofit:
                    if j[0].isnumeric():
                        salaries_yearly_with_decimal += j
                # Remove last three chars of the salaries yearly
                # We remove the decimal part and "," or "." sing
                # And we cast the string as an integer
                salaries_yearly = int(salaries_yearly_with_decimal[:-3])                
                break

        # Percent of income spent on salaries        
        # Make sure not to divide by 0
        # You know how if elif elif else works - statements under first true conditions are evaluated, and the cluase stops
        if income_yearly < salaries_yearly:
            percent_of_income_spent_on_salaries = "Salaries are bigger than income!"
        elif salaries_yearly == 0:
            percent_of_income_spent_on_salaries = "Nonprofit did not spend anything on salaries!"
        elif salaries_yearly != 0:
            percent_of_income_spent_on_salaries = round(salaries_yearly/income_yearly, 3)
        
        
                
    # I need to use special sign between columns since ',' sign is used in names of some nonprofits 
    collection_of_nonprofit_names.append([name_of_nonprofit,";", year_of_the_statement, ";", income_yearly, ";", salaries_yearly , ";", percent_of_income_spent_on_salaries,";", input_filename])

print("\n'n\n\n")

# Adding the names of nonprofits with no statements
with open("nie działa.txt") as f:
    x = f.readline()

for i in (x.split(",")):
    name_of_nonprofit = i
    # Name clensing
    if name_of_nonprofit[0].isalpha() == False:
        name_of_nonprofit = name_of_nonprofit.replace('"','')
        name_of_nonprofit = name_of_nonprofit.replace('[','')
        name_of_nonprofit = name_of_nonprofit.replace(']','')
    year_of_the_statement = "Nonprofit did not publish the statement for this year"
    income_yearly = "Nonprofit did not publish the statement for this year"
    salaries_yearly = "Nonprofit did not publish the statement for this year"
    percent_of_income_spent_on_salaries = "Nonprofit did not publish the statement for this year"
    input_filename = "Nonprofit did not publish the statement for this year"

    collection_of_nonprofit_names.append([name_of_nonprofit,";", year_of_the_statement, ";", income_yearly, ";", salaries_yearly , ";", percent_of_income_spent_on_salaries,";", input_filename])

output_filename = "output.csv"

with open(output_filename, "w", newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["Name of nonprofit",";","Year of statement",";", "Income yearly",";", "Salaries yearly",";", "Percent spent on salaries", ";", "Name of the file"])
    writer.writerows(collection_of_nonprofit_names)
