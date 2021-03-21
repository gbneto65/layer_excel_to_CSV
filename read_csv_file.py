# Layers project V2

import pandas as pd
import os
from setup_parameters import soft_version, working_directory, csv_file_name, sound_error, intro_text, error_exit, \
    datetime_now, error_exit


# class to manage the CSV file created by DatabaseExcelRead() in Database_read_process.py
# CSV file contains all info from excel file - the original databse for layers genetics paramters

class Csv_file():
    csv_file_name = csv_file_name  # file name as class variable

    def __init__(self):
        pass

    def csv_verify_if_exist(self):  # verify if CSV file exit on the working directory

        if os.path.isfile(csv_file_name):
            print(f'CSV File "{csv_file_name}" exist')
            return True
        else:
            print('ERROR: CSV File does not exist')
            sound_error()  # call a function for sound error
            error_exit()
            return False

        # read CSV file and store it in dta_df (df variable)

    def csv_read(self):
            if os.path.isfile(csv_file_name):
                print(f'CSV File "{csv_file_name}" exist')

            try:
                self.dta_df = pd.read_csv(csv_file_name)
                print('\nColumns Names & Types\n')
                print(self.dta_df.dtypes)
                return self.dta_df

            except:
                sound_error()
                print(f'ERROR: CSV File does not exist on {working_directory}')
                print(f'\n Run again the "database_read_process.py" to generated a new CSV file {csv_file_name}')
                error_exit()


"""
	def get_csv_status (self):
		return self.csv_verify_if_exist(self)
"""

"""
	# read CSV file and store it in dta_df (df variable)
	class Csv_read():
		#a = Csv_file()
		
		def __init__(self):
			try:
				self.dta_df = pd.read_csv(csv_file_name)
				print('\nColumns Names & Types\n')
				print(self.dta_df.dtypes)
			except:
				sound_error()
				print(f'ERROR: CSV File does not exist on {working_directory}')
				print(f'\n Run again the "database_read_process.py" to generated a new CSV file {csv_file_name}')
				error_exit()

"""

a = Csv_file()
b = a.csv_read
print(b)

# print(a.show())


"""
intro_text('Read_CSV_File')
csv_file = Csv_file()


if  csv_file.csv_verify_if_exist():
	csv_file.csv_read()

"""
