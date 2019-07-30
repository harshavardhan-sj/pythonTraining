# -------------------------------------------------------------------------
#
# Copyright Altran, 2019
#
# -------------------------------------------------------------------------
#
# Description:
#    Python script to:
#           1. Read the csv and print all the Region in
#           a list and sort them in ascending order.
#           2. List all the country name where the sale
#           channel is online from the given csv file
#           3. Write all the Asia region items
#           into the new csv file.
#           4. Write all the items into a new csv for
#           the items having valid ship date.
#
# -------------------------------------------------------------------------
#Referal links:
#
#       https://stackoverflow.com/questions/15559812/sorting-by-specific-column-data-using-csv-in-python
#
#       https://stackoverflow.com/questions/29310792/how-to-save-a-list-as-a-csv-file-with-python-with-new-lines
#
#       https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
#
#       https://docs.python.org/2/library/csv.html
# -------------------------------------------------------------------------

#We can import or export spreadsheets and databases for
#use in the Python interpreter using CSV module.
import csv

#pandas represent the data in a DataFrame form and provides
#extensive usage for data analysis and data manipulation.
import pandas as pd

#In Python, date, time and datetime classes provides a number
#of function to deal with dates, times and time intervals.
import datetime


class Task_csv:


    def sort_region(self):
        """
            Method to Read the csv and print all the Region
            in a list and sort them in ascending order.
        """
        collected = []
        df = pd.read_csv("C:\Users\gur53870\Documents\\100 Sales Records.csv")
        df = df.sort_values('Region')
        df.to_csv('full_list_sorted.csv')

        with open("C:\\Python27\\Full_List_sorted.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            print("Listing sorted Regions in ascending order:")
            print("**************************************************")
            print("["),
            for row in reader:
                collected.append(row['Region'])
        print ",".join(collected),
        print("]")
        csvfile.close()
        print("********************************************************\n")

    def online_sale_channel(self):
        """
            Method to List all the country name where the
            sale channel is online from the given csv file.
        """
        with open("C:\\Users\\gur53870\\Documents\\100 Sales Records.csv") \
             as csvfile:
            reader = csv.DictReader(csvfile)
            print("Listing country names whose sale channel is online:")
            print("***************************************************")

            Country = []
            print("["),
            for row in reader:
                if(row['Sales Channel'] == 'Online'):
                    Country.append(row['Country'])
        print ",".join(Country),
        print("]")
        csvfile.close()
        print("*******************************************************\n")

    def asia_region_items(self):
        """
            Method to Write all the Asia region
            items into the new csv file.
        """
        with open("C:\\Users\\gur53870\\Documents\\100 Sales Records.csv") \
            as csvfile:
            reader = csv.DictReader(csvfile)
            file_path = "C:\\Python27\\asia_item_type.csv"
            listed = []

            for row in reader:
                if(row['Region'] == 'Asia'):
                    listed.append(row['Item Type'])

        df = pd.DataFrame(listed)
        df.to_csv('asia_item_type.csv')
        csvfile.close()
        print("********************************************************")
        print("Asia region items added into the asia_item_type.csv file")
        print("new file is created in {}".format(file_path))
        print("******************************************************\n")

    def valid_ship_date(self):
        """
            Method to  Write all the items into a new
            csv for the items having valid ship date.
        """
        with open('C:\\Users\\gur53870\\Documents\\100 Sales Records.csv') \
            as csvfile:
            reader = csv.DictReader(csvfile)

            valid_date = []
            items = []
            file_path = "C:\\Python27\\valid_dates_items.csv"
            print("*****************************************************")
            print("Items with valid ship date added to valid_dates_items.csv")
            print("new file is created in {}".format(file_path))
            print("**************************************************")

            for row in reader:
                my_date = row['Ship Date']
                #print(my_date)
                dateparts = my_date.split('/')
                if((dateparts[0] > 12) and (dateparts[0] < 1)):
                   print("invalid date")
                elif((dateparts[1] > 31) and (dateparts[1] < 1)):
                    print("invalid month")
                #elif((dateparts[2] > 2019)):
                    #print("invalid year")
                else:
                    valid_date.append(my_date)
                    items.append(row['Item Type'])
        csvfile.close()
        df = pd.DataFrame(items)
        df.to_csv('valid_dates_items.csv')

def main():

#creating a object for methods
    csv_obj = Task_csv()

    csv_obj.sort_region()

    csv_obj.online_sale_channel()

    csv_obj.asia_region_items()

    csv_obj.valid_ship_date()

if __name__ == "__main__":
    main()

