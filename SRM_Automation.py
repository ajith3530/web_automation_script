#Pranav Code
import xlrd                                         #to access xl file related commands, use xlrd library
workbook=xlrd.open_workbook("Dataset.xlsx")         #creating an object to access the workbook
worksheet=workbook.sheet_by_name("Data")            #creating an object to access the worksheet
rows=worksheet.nrows
columns=worksheet.ncols                             #to access the number of rows and columns
row_data=list()                                     #creating lists for data storage
column_data=list()
for y in range(columns):                            #for loop to access the first row
    row_data.append(worksheet.cell(0,y).value)
    if worksheet.cell(0,y).value=="Market":
        column_num=y
for x in range(rows):
    column_data.append(worksheet.cell(x,column_num).value)

for y in range(columns):
     var=str(worksheet.cell(1,y).value)
     if var.isalnum()==True:
         print(var)     

print(row_data)
print(column_data)
#Pranav Code
