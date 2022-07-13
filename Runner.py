print("Extracting...")
# import data
import xlrd

# Give the location of the file
loc = ("Databases/Dataset1/False.csv")
workbook = xlrd.open_workbook(loc)
sheet = workbook.sheet_by_index(0)
print("Finished")
 
# Extracting number of rows
print(sheet.nrows)
