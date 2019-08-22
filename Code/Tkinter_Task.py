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
import Tkinter as tk

#Import everything from tkinter module.
from Tkinter import *

#Importing class Task_csv from csv_task.py
from CSV_Task import Task_csv

#Importing class Task_01 from Gmail_automation_1.2.py
from Gmail_Automation import Task_01

#Importing class Task_02 from python_file_task.py
from Files_Task import Task_02

#Importing class Task_02 from python_file_task.py
from Excel_Task import Excel_Task

#Getting the current working directory
cur_dir = os.getcwd()

#File path of CSV file operation task.
csv_path = os.path.join(cur_dir,"Code","CSV_Task.py")

#File path of Gmail Automation task.
gmail_path = os.path.join(cur_dir,"Code","Gmail_Automation.py")

#File path of Files and directories operation task.
file_path = os.path.join(cur_dir,"Code","Files_Task.py")

#File path of Excel file operation task.
excel_path = os.path.join(cur_dir,"Code","Excel_Task.py")



#Class to create GUI Application
class GUI_task:


    def __init__(self):

        """To initialize and init gets called automatically
            whenever we create an object.
            
            :param: None
            :return: None

        """
        #To create a GUI window 
        self.root = Tk()

        #To set the title of GUI window
        self.root.title("Task execution window")

        #To set the background colour of GUI window 
        self.root.configure(background="light blue")
        

        #Adding csv button to the main window.
        csvbutton = tk.Button(self.root,text="CSV",bg='blue',width=40,fg='white',command= self.run_csv_task)
        csvbutton.pack()

        #Adding gmail button to the main window.
        gmailbutton = tk.Button(self.root,text="Gmail",bg='blue',width=40,fg='white',command= self.run_gmail_task)
        gmailbutton.pack()

        #Adding file button to the main window.
        filebutton = tk.Button(self.root,text="FilesOperation",bg='blue',width=40,fg='white',command= self.run_files_task)
        filebutton.pack()

        #Adding excel button to the main window.
        excelbutton =tk.Button(self.root,text="Excel",bg='blue',width=40,fg='white',command= self.run_excel_task)
        excelbutton.pack()
        
        #Adding Exit button to the main window.
        exitbutton = tk.Button(self.root,text="Exit",bg='blue',width=40,fg='white',command= self.quit_program)
        exitbutton.pack()

        #To wait for an event to occur and process the event
        #till the window is not closed. 
        self.root.mainloop()
              
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

    def quit_program(self):
        """
            To Create an exit button.
            
            :param: None
            :return: None
        """
        #To close the window in Tkinter
        self.root.destroy()
   

def main():
    
    #Creating object for Class GUI_task
    GUI_task_obj = GUI_task()

    
if __name__ == "__main__":
    main()
