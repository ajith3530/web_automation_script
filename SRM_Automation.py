#<Anirudhh Code>
from selenium import webdriver #import webdriver from selenium
path='chromedriver' #initialize the path to chromedriver to access chrome
driver=webdriver.Chrome('F:\\Python\\chromedriver_win32\\chromedriver.exe') #declare the chromedriver path in system
url='https://en.wikipedia.org/wiki/2011_Census_of_India' #create a variable that stores the url link of the website that needs to be scraped
driver.get(url) #access the url link
 #code to scrap table header
row_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr")) #row count using table row child
col_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr[1]/th")) #column count using table header child
print("Number of Rows ",row_count)
print("Number of Columns ",col_count)
first_part="//*[@id='mw-content-text']/div/table[9]/tbody/tr[1]/th[" #variable to store the xpath
second_part="]"
for n in range(1,col_count+1):
    final_path=first_part+str(n)+second_part #loop from th[1] through th[col_count+1]
    table_data=driver.find_element_by_xpath(final_path).text #store the collected data in a local variable
    print(table_data,end=" ") #print the collected [table header] data
print('\n')
    #code to scrap table data
row_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr"))
col_count=len(driver.find_elements_by_xpath("//*[@id='mw-content-text']/div/table[9]/tbody/tr[2]/td"))
first_part="//*[@id='mw-content-text']/div/table[9]/tbody/tr[" #variable to store the table row for the loop
second_part="]/td[" #variable to store table data for the loop
third_part="]"
for n in range(1,row_count): #loop from tr[1] through tr[row_count], collection of table row
    for m in range(1,col_count+1): #loop from td[1] through td[col_count+1], collection of data corresponding to tr[n]
        final_path=first_part+str(n+1)+second_part+str(m)+third_part #start the loop from tr[2] as tr[1] is already collected
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
