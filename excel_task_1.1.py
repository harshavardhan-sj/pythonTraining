# ---------------------------------------------------------------------
#
# Copyright Altran, 2019
#
# ---------------------------------------------------------------------
#
# Description:
#    Python script to:
#           1. Read the excel file and print the first Row data
#              in a list(Header Row usually)
#           2. Read the excel file and print the first column data
#              in a list
#           3. Read the excel file and get the column data
#              and write into the new excel file
#           4. Read the excel file and write all the data
#              to the new excel file
#
# ---------------------------------------------------------------------
#
# Referal links:
#           1. Read the excel file and print the first Row data
#              in a list(Header Row usually)
#              https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/
#
#           2. Read the excel file and print the first column data
#              in a list
#              https://www.geeksforgeeks.org/python-reading-excel-file-using-openpyxl-module/
#
#           3. Read the excel file and get the column data and
#              write into the new excel file
#              https://youtube.be/-0NwrcZOKhQ
#
#           4. Read the excel file and write all the data
#              to the new excel file
#              https://youtube.be/-0NwrcZOKhQ
#
# ---------------------------------------------------------------------

#importing the required modules

#pandas is an open source, BSD-licensed library
#providing high-performance, easy-to-use data structures and
#data analysis tools for the Python programming language.
import pandas as pd

#openpyxl is a Python library
#It read/write Excel xlsx/xlsm/xltx/xltm
import openpyxl

#OS module provides functions for interacting with the operating system
import os


#Class for processing excel file
class Excel_Task:


    def extract_first_row_data(self, input_filepath):
        """
            Reads the excel file and print
            the first Row data in a list

            :param str input_filepath: File path for input file
            :return: None
            :raises IOError: If the input file was not found
        """
        print("\n         **********Fist Row Data***********       \n")
        try:
            #Loading the specified excel file
            wb = openpyxl.load_workbook(input_filepath)
            print("\nWorkbook loaded successfully!")

            #Getting the required sheet from the excel file
            sheet = wb.get_sheet_by_name('SalesOrders')
            #Getting the required row
            row_cells = sheet[1]

            #List to hold all the data elements of the first row
            row_collection = []

            #Iterating over the first row
            for cellObj in row_cells:
                #Appending each row element to the list
                row_collection.append(str(cellObj.value))

            print(row_collection)

        except IOError as fnf_error:
            print(fnf_error)
            print("\nUnable to load workbook")

    def extract_first_column_data(self, input_filepath):
        """
            Reads the excel file and print
            the first Column data in a list

            :param str input_filepath: File path for input file
            :return: None
            :raises IOError: If the input file was not found
        """
        print("\n         **********Fist Column Data***********       \n")
        try:
            #Loading the specified excel file
            wb = openpyxl.load_workbook(input_filepath)
            print("\nWorkbook loaded successfully!")

            #Getting the required sheet from the excel file
            sheet = wb.get_sheet_by_name('SalesOrders')
            #Getting the required column
            column_cells = sheet['A']
            #List to hold all the data elements of the first column
            column_collection = []

            #Iterating over the first column
            for cellObj in column_cells:
                #Appending each column element to the list
                column_collection.append(str(cellObj.value))


            print(column_collection)

        except IOError as fnf_error:
            print("\nUnable to load workbook")
            print(fnf_error)

    def column_data_into_new_file(self, input_filepath):
        """
            Reads the excel file and get
            the column data and write into the new excel file

            :param str input_filepath: File path for input file
            :return: None
            :raises IOError: If the input file was not found
        """
        print("\n*****************************************************")
        print("Extracting a column data and writing it into new file")
        print("*****************************************************\n")
        try:
            #To read and store entire data in the excel sheet into dataframe
            df = pd.read_excel(input_filepath, "SalesOrders",index=False)
            new_output_file_path = os.path.join("C:/","Python27","new_col.xlsx")

        #To write the data in dataframe into newly created excel sheet
        #Only the specified column has been written into new excel sheet
            df.to_excel(new_output_file_path, sheet_name="SalesOrders",
                    columns=['Region'], index=False)
            print("\nWorkbook loaded successfully!")
            print("Column has been successfully written into new file")
            print("Checkout new file at {}". format(new_output_file_path))

        except IOError as fnf_error:
            print("\nUnable to load workbook")
            print(fnf_error)


    def write_data_into_new_file(self, input_filepath):
        """
            Reads the excel file and
	    write all the date into the new excel file

	    :param str input_filepath: File path for input excel file
	    :return: None
            :raises IOError: If the input file was not found
        """
        print("\n*****************************************************")
        print("Extracting all data and writing it into new excel file")
        print("*****************************************************\n")
        try:
            #Reading the required sheet from the excel file
            #storing it in the dataframe
            df_1 = pd.read_excel(input_filepath, "Instructions", index=False)
            df_2 = pd.read_excel(input_filepath, "SalesOrders", index=False)
            df_3 = pd.read_excel(input_filepath, "SampleNumbers", index=False)
            df_4 = pd.read_excel(input_filepath, "MyLinks", index=False)

            #New file path
            new_file_path = os.path.join("C:/","Python27","new_excel_file.xlsx")

            #Writing specified sheets of excel file into newly created excel file
            with pd.ExcelWriter(new_file_path) as writer:
                df_1.to_excel(writer, "Instructions", index=False)
                df_2.to_excel(writer, sheet_name="SalesOrders", index=False)
                df_3.to_excel(writer, "SampleNumbers", index=False)
                df_4.to_excel(writer, "MyLinks", index=False)

            print("SampleData.xlsx file has been wriiten into new file")
            print("Checkout the new file at {}". format(new_file_path))

        except IOError as fnf_error:
            print("\nUnable to load workbook")
            print(fnf_error)

def main():

    #Input excel file path
    input_filepath = os.path.join("C:/","Python27","SampleData.xlsx")

    #Object creation
    excel_obj = Excel_Task()

    #Calling the method extract_first_row_data() from object excel_obj
    excel_obj.extract_first_row_data(input_filepath)

    #Calling method extract_first_column_data() from object excel_obj
    excel_obj.extract_first_column_data(input_filepath)

    #Calling method column_data_into_new_file() from object excel_obj
    excel_obj.column_data_into_new_file(input_filepath)

    #Calling method write_data_into_new_file() from object excel_obj
    excel_obj.write_data_into_new_file(input_filepath)

if __name__ == "__main__":
    main()



