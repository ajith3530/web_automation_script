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
#Varun code
from selenium import webdriver
import time
driver = webdriver.Chrome('C:\\# your root directory')
driver.maximize_window()
driver.get('https://academia.srmuniv.ac.in')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
driver.implicitly_wait(10)
driver.find_element_by_name('username').send_keys('#your srmID')
driver.find_element_by_name('password').send_keys('#your password')
a = find_element_by_xpath("//*[@id='signinForm']/div[5]/input")
c.click()
time.sleep(5)
driver.quit()
#Varun code
