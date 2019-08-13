# -------------------------------------------------------------------------
#
# Copyright Altran, 2019 
#
# -------------------------------------------------------------------------
# Description:This python script includes following tasks.
#    To create a tkinter GUI application using tkinter module with the below details.
#       1.Application should have the below buttons 
#            Gmail , FilesOperation,  CSV and Excel
#       2.when you click the button it should execute the respective task script.
#
# -------------------------------------------------------------------------
#   Referal links:
#   https://www.python-course.eu/tkinter_buttons.php
#   
#   https://stackoverflow.com/questions/7420937/run-program-in-python-shell
#
#   https://www.geeksforgeeks.org/python-gui-tkinter/
# -------------------------------------------------------------------------


#The sys module provides information about constants,
#functions and methods of the Python interpreter.
import sys

# OS module provides a way of using operating system dependent functionality.
import os

#Tkinter is an inbuilt Python module used to create simple GUI apps.
import Tkinter

#Import everything from tkinter module.
from Tkinter import *

#Importing class Task_csv from csv_task.py
from try_csv_task import Task_csv

#Importing class Task_01 from Gmail_automation_1.2.py
from Gmail_automation_1_2 import Task_01

#Importing class Task_02 from python_file_task.py
from files_dir_task import Task_02

#Importing class Task_02 from python_file_task.py
from excel_file_task import Excel_Task



#File path of CSV file operation task.
csv_path = os.path.join("pythonTraining","Code","CSV_Task.py")

#File path of Gmail Automation task.
gmail_path = os.path.join("pythonTraining","Code","Gmail_Automation.py")

#File path of Files and directories operation task.
file_path = os.path.join("pythonTraining","Code","Files_Task.py")

#File path of Excel file operation task.
excel_path = os.path.join("pythonTraining","Code","Excel_Task.py")


#Class to create GUI Application
class GUI_task:


    def __init__(self, master):

        """To initialize and init gets called automatically
            whenever we create an object.
            
            :param str master:  The main window.
            :return: None

        """
        #Used for grouping and organizing the widgets.
        frame = Frame(master)
        
        #Pack organizes the widgets in blocks before placing
        #in the parent widget.
        frame.pack()

        #Adding csv button to the main window.
        self.csvbutton = Button(frame,text="CSV",bg='blue',width=40,fg='white',command= self.run_csv_task)
        self.csvbutton.pack()

        #Adding gmail button to the main window.
        self.gmailbutton = Button(frame,text="Gmail",bg='blue',width=40,fg='white',command= self.run_gmail_task)
        self.gmailbutton.pack()

        #Adding file button to the main window.
        self.filebutton = Button(frame,text="FilesOperation",bg='blue',width=40,fg='white',command= self.run_files_task)
        self.filebutton.pack()

        #Adding excel button to the main window.
        self.excelbutton = Button(frame,text="Excel",bg='blue',width=40,fg='white',command= self.run_excel_task)
        self.excelbutton.pack()
              
    def run_csv_task(self):
        """
            To Create a button and Execute CSV File task.
            
            :param: None
            :return: None
            :raises IOError: If the given file path is incorrect.
        """
        print("executing csv file operations program")
        print("*************************************\n")
        try:
            execfile(csv_path)
        except IOError as fnf_error:
            print(fnf_error)
    
    def run_gmail_task(self):
        """
            To Create a button and Execute Gmail Automation task.
            
            :param: None
            :return: None
            :raises IOError: If the given file path is incorrect.
        """
        print("executing Gmail Automation program")
        print("*************************************\n")
        try:
            execfile(gmail_path)
        except IOError as fnf_error:
            print(fnf_error)  

    def run_files_task(self):
        """
            To Create a button and Execute files and directories task.
            
            :param: None
            :return: None
            :raises IOError: If the given file path is incorrect.
        """
        print("executing files and directories program")
        print("*************************************\n")
        try:
            execfile(file_path)
        except IOError as fnf_error:
            print(fnf_error)

    def run_excel_task(self):
        """
            To Create a button and Execute Excel files task.
            
            :param: None
            :return: None
            :raises IOError: If the given file path is incorrect.
        """
        print("executing Excel files operation program")
        print("*************************************\n")
        try:
            execfile(excel_path)
        except IOError as fnf_error:
            print(fnf_error)

def main():


    #To create a GUI window 
    top=Tk()

    #To set the title of GUI window
    top.title("Task execution window")

    #To set the background colour of GUI window 
    top.configure(background="light blue")
    
    #Creating object for Class GUI_task
    GUI_task_obj = GUI_task(top)

    #To wait for an event to occur and process the event
    #till the window is not closed. 
    top.mainloop()
           
    
if __name__ == "__main__":
    main()
    

    
