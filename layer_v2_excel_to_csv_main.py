# Layers project V2
# app to convert excel file database to CSV file.
# the DF excel filename should be informed in the module 'setup_parameter.py'


from database_read_process import DatabaseExcelRead
from setup_parameters import datetime_now, sound_error, error_exit, intro_text, csv_file_name
from read_csv_file import Csv_file




intro_text('Read Database from Excel File')
database_read = DatabaseExcelRead()

print('Date: ' + str(datetime_now()))
# print(f'software version (GIT-SHA) : {database_read.soft_version}')
# print(f'Sheet names found in the excel file: {sheet_names}')
# sheets_names = database_read.get_sheet_names()
# print(f'Sheet names found in the excel file: {sheets_names}')

if database_read.test_if_excel_exist():
    try:
        sheets_names = database_read.get_sheet_names()
        print(f'Sheet names found in the excel file: {sheets_names}\n')
    except:
        print("ERROR - cannot get sheetnames")
        error_exit()
else:
    error_exit()

# create csv file - used for others modules

database_read.read_excel_file().to_csv(csv_file_name)
# test if CSVfile was created and exist in the working folder
csv_file = Csv_file()

if csv_file.csv_verify_if_exist():
    print('CSV successfully created\n')
else:
    sound_error()
    print('Error: cannot create CSV file\n')
    error_exit()

print('\n**** End of CSV process creation *****')
# know issues: it seems the Openpyxl module is corrupting the xlsx files.
