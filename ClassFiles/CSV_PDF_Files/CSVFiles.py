"""             Working with CSV files
CSV stands for comma separated value.
CSV file data fields are often seperated by a comma.
CSV file format can store tabular data like a spreadsheet or database file.
                READING A CSV FILE
Python csv library module is used to interact with csv files.
CSV module has functionality to read and write to CSV files.
The reader object from the csv module is used to read a csv file.
The Python built-in open() function is used to open the csv file which returns a file object.
"""
import csv
with open('Names.csv','rt')as file:
    csv_rows = csv.reader(file)
    for row in csv_rows:
        print(row)

