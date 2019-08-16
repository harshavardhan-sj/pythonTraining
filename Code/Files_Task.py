# -------------------------------------------------------------------------
#
# Copyright Altran, 2019
#
# -------------------------------------------------------------------------
#
# Description:
#    Python script to:
#           1)Get all files count and directories count from a root folder.
#           2)Find the duplicate files from a root folder.
#           3)Find all the word counts in a specific file.
#           4)Replace all the word with first letter capital in a given file.
#           5)Search a specific file from root folder.
#           6)Remove the given string in the file wherever it is present.
# -------------------------------------------------------------------------
#Referal links:
#           1)Get all files count and directories count from a root folder.
#           https://stackoverflow.com/questions/2632205/how-to-count-the-number-of-files-in-a-directory-using-python

#           
#           2)Find the duplicate files from a root folder.
#           https://gist.github.com/vinovator/a2ba7306e829bf3a9010
#           
#           3)Find all the word counts in a specific file.
#           https://www.sanfoundry.com/python-program-count-number-words-characters-file/
#       
#           4)Replace all the word with first letter capital in a given file.
#           https://stackoverflow.com/questions/1549641/how-to-capitalize-the-first-letter-of-each-word-in-a-string-python

#
#           5)Search a specific file from root folder.
#           https://stackoverflow.com/questions/1724693/find-a-file-in-python
#
#           6)Remove the given string in the file wherever it is present.
#           https://stackoverflow.com/questions/7356043/python-deleting-specific-strings-from-file

#
# -------------------------------------------------------------------------
# OS module in Python provides a way of using operating system dependent functionality
import os

#This module implements a common interface to many different secure hash
#and message digest algorithms such as MD5, SHA1, SHA224, SHA256, SHA384.
import hashlib

#Returns a new dictionary-like object.Defaultdict is a subclass of dict class.
#It overrides one method and adds one writable instance variable.
from collections import defaultdict

#Csv module implements classes to read and write tabular data in CSV format.
import csv

#Getting the current working directory
cur_dir = os.getcwd()

class Task_02:


    def file_folder_count(self):
        """
            To Get all files count and directories
            count from a root folder.
            
            :params: None
            :return: None

        """
        print("***********To count number of files and directories**********")
        
        files = folders = 0

        for _, dirnames, filenames in os.walk("Files_Task", topdown=True):
          # ^ this idiom means "we won't be using this value"
            files += len(filenames)
            folders += len(dirnames)

        print("File count is {}" .format(files))
        print("Folder count is {}" .format(folders))
        print("\n")
       
    def duplicate_files(self):
        """
            To Find the duplicate files from a root folder.

            :params: None
            :return: None
        """
        src_folder = os.path.join(cur_dir,"Helper","Files_Task")
        print("***************To list duplicate files******************")

        def generate_md5(fname, chunk_size=1024):

            """
                To generate md5 checksum of the file.
                
                :param str fname: file path
                :return: hex checksum

            """
          
            hash = hashlib.md5()

            with open(fname, "rb") as f:

                # Read the 1st block of the file
                chunk = f.read(chunk_size)

                # Keep reading the file until the end and update hash
                while chunk:
                    hash.update(chunk)
                    chunk = f.read(chunk_size)

                # Return the hex checksum
            return hash.hexdigest()


        if __name__ == "__main__":
    
            md5_dict = defaultdict(list)
            file_types_inscope = ["ppt", "pptx", "pdf", "txt", "html",

                                      "mp4", "jpg", "png", "xls", "xlsx", "xml",

                                      "vsd", "py", "json"]

                # Walk through all files and folders within directory
            for path, dirs, files in os.walk(src_folder):
                print("Analyzing {}".format(path))

                for each_file in files:

                    if each_file.split(".")[-1].lower() in file_types_inscope:

                            # The path variable gets updated for each subfolder
                        file_path = os.path.join(os.path.abspath(path), each_file)

                            #More files with same checksum append to list
                        md5_dict[generate_md5(file_path)].append(file_path)



                # Identify keys (checksum) having more than one values (file names)
            duplicate_files = (
                val for key, val in md5_dict.items() if len(val) > 1)

                # Write the list of duplicate files to csv file
            with open("duplicates.csv", "w") as log:
               
                    # Lineterminator added for windows as it inserts blank rows otherwise
                csv_writer = csv.writer(log, quoting=csv.QUOTE_MINIMAL,
                                        delimiter=",",lineterminator="\n")
                header = ["File Names"]
                csv_writer.writerow(header)

                for file_name in duplicate_files:
                    csv_writer.writerow(file_name)

            print("Duplicate files have been successfully listed")
            print("checkout in path {}".format(os.path.join("C:/","Python27","duplicates.csv")))
            print("\n")
            
            
    def word_count(self):
        """
            To find all the word counts in a specific file.

            :params: None
            :return: None
        """
        print("**************To display word count in a file****************")
        fname = os.path.join(cur_dir,"Helper","Files_Task","word_count.txt")
        num_words = 0
         
        with open(fname, 'r') as f:
            contents = f.read()
            print("File contents:")
            print(contents)
            
        with open(fname, 'r') as f:
            for line in f:
                words = line.split()
                num_words += len(words)
                
        print("Number of words:")
        print(num_words)
        f.close()
        print("\n")
        
    def capitalise_first_letter(self):
        """
            To replace all the word with first
            letter capital(Title) in a given file.

            :params: None
            :return: None
        """
        print("****To capitalise first letter of all the words in file*****")
        file_name_path = os.path.join(cur_dir,"Helper","Files_Task","capitalise_first_letter.txt")
        
        with open(file_name_path, 'r') as fp:
            file_content = fp.read()
            print("File contents before capitalising:")
            print(file_content)
            
            output_str = file_content.title()
        print("File contents after capitalising:")
        print(output_str)
        print("\n")
        
    def search_file(self):
        """
            To search a specific file from root folder

            :params: None
            :return: None
        """
        print("***************To search a specific file******************")
        print("Searching the file.....{}", format("dups_02.txt"))
        #time.sleep(10)
        path = os.path.join(cur_dir,"Helper","Files_Task")
        required_file_name = "dups_02.txt"

        def find_required_file(name, path):
            for root, dirs, files in os.walk(path):
                if name in files:
                    return os.path.join(root, name)
         

        if __name__ == "__main__":
            required_file_path = find_required_file(required_file_name, path)
            print("The required file {} was found".format("dups_02.txt"))
            print("The path {}\n".format(required_file_path))
            
    def remove_string(self):
        """
            To remove the given string in the
            file wherever it is present.

            :params: None
            :return: None
        """
        print("*******To remove specific string from particular file*******")
        
        file_path = os.path.join(cur_dir,"Helper","Files_Task","remove_string.txt")
        string_to_be_removed = ['hello']
        print("The string to be removed is : {}".format(string_to_be_removed))
        lst = []
                  
        file_pointer = open(file_path,"r")
        print("File contents before removing the string")
        string_file_contents = file_pointer.read()
        print(string_file_contents)
        

        file_pointer = open(file_path,"r")
        for line in file_pointer:
            for word in string_to_be_removed:
                if word in line:
                    line = line.replace(word,'')
            lst.append(line)

        file_pointer = open(file_path,"w")
        for line in lst:
            file_pointer.write(line)

        file_pointer = open(file_path,"r")
        string_file = file_pointer.read()
        print("File contents after removing the string")
        print(string_file)
        file_pointer.close()
        print("\n")

def main():
 
    file_task_obj = Task_02()

#calling method file_folder_count() from object file_task_obj    
    file_task_obj.file_folder_count()

#calling method duplicate_files() from object file_task_obj  
    file_task_obj.duplicate_files()
    
#calling method word_count() from object file_task_obj  
    file_task_obj.word_count()
    
#calling method capitalise_first_letter() from object file_task_obj  
    file_task_obj.capitalise_first_letter()
    
#calling method search_file() from object file_task_obj  
    file_task_obj.search_file()
    
#calling method remove_string() from object file_task_obj  
    file_task_obj.remove_string()
   

if __name__ == "__main__":
    main()

