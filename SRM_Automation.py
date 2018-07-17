#<Anirudhh Code>
from selenium import webdriver
path='chromedriver'
driver=webdriver.Chrome('F:\\Python\\chromedriver_win32\\chromedriver.exe')
url='https://en.wikipedia.org/wiki/2011_Census_of_India'
driver.get(url)
row_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr"))
col_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr[1]/th"))
print("Number of Rows ",row_count)
print("Number of Columns ",col_count)
first_part="//*[@id='mw-content-text']/div/table[9]/tbody/tr[1]/th["
second_part="]"
for n in range(1,col_count+1):
    final_path=first_part+str(n)+second_part
    table_data=driver.find_element_by_xpath(final_path).text
    print(table_data,end=" ")
print('\n')
row_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr"))
col_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr[2]/td"))
first_part="//*[@id='mw-content-text']/div/table[9]/tbody/tr["
second_part="]/td["
third_part="]"
for n in range(1,row_count):
    for m in range(1,col_count+1):
        final_path=first_part+str(n+1)+second_part+str(m)+third_part
        table_data=driver.find_element_by_xpath(final_path).text
        print(table_data,end="  ")
    print("")
print('\n')
#<\Anirudhh Code>
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
    row_data.append(worksheet.cell(x,column_num).value)
print(row_data)
print(column_data)
#Pranav Code
