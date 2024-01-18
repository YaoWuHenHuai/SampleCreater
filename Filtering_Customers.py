import pandas
import os
import numpy
from pathlib import Path
from datetime import date
from datetime import datetime
from rich import print
import sys

WorkingDirectory = (r"C:\Users\杜甫\Desktop\BaseQueryStructure\\")
os.chdir(WorkingDirectory)
#Folder for each customer, each on will be extracted from the selected source
FiltersList = "Customers"

folder_path = os.path.join(WorkingDirectory, FiltersList)
if os.path.exists(FiltersList):
    print(FiltersList + " Already there")
else:
    os.mkdir(FiltersList)
    print(FiltersList + " has been created")

os.chdir(folder_path)
print(("following is the current working directory ")+ os.getcwd())


#Will make Dataframe out of the source 

SourceFile = "AceptanceReport"
os.chdir(WorkingDirectory)


#To get a list for unique values within customer Column , although there is originally more customers, we will only grab the ones within the file 
Unique_Values_List = []
def get_unique_values_list_within_df(x):
    if x.endswith(".xlsx"):
            df = pandas.read_excel(x, engine="openpyxl")
            print("Reading " + x +" dataframe")
            print(df.columns)
            c = []
            for y in df["Customer"].iloc:
                if y not in c:
                    c.append(y)
                    Unique_Values_List.append(y)
    print()
    print("The following are the unique values within Customer Column from the df was took from " + x)
    print(c)
    
#This example we get those unique values from the column from the AceptanceReport
x = "AceptanceReport.xlsx"
get_unique_values_list_within_df(x)
Data_Directory = (r"C:\Users\杜甫\Desktop\Projects\ReportsAutomation\\")
os.chdir(Data_Directory)
useless_df = pandas.DataFrame({"Column":Unique_Values_List})
#This is for further is , to storage within the server
useless_df.to_csv("lists.csv", index= False)



#In order to express current directory file     
z = []
for x in os.listdir(WorkingDirectory):
    if x.endswith(".xlsx"):
        z.append(x)
print("Following are the .xlsx files within the current working directory")
print(z)


print()
print("Will get into the following directory ")
print((os.path.join(WorkingDirectory + FiltersList)))
os.chdir(os.path.join(WorkingDirectory + FiltersList))


#Here can decide which file we will be reading from , same fr
Excel_File_Name = "AceptanceReport.xlsx"
print()
print("Working with " + Excel_File_Name)
print(Excel_File_Name)
File_To_Read = os.path.join(WorkingDirectory + Excel_File_Name)
Data_Directory = (r"C:\Users\杜甫\Desktop\Projects\ReportsAutomation\\")
os.chdir(Data_Directory)
df = pandas.read_excel(File_To_Read, engine="openpyxl")
print(df)

os.chdir(os.path.join(WorkingDirectory + FiltersList))
#Values we got into the Unique List, will be used here now 
print(Unique_Values_List)


os.chdir(os.path.join(WorkingDirectory , FiltersList))
to_delete_list = []
some_list = []
Will_Be_Reading_File = "AceptanceReport.xlsx"



#Here we clean the directory, we ask for security purposses
print("You are currently working within " + os.path.join(WorkingDirectory, FiltersList))
print("the following are the files within " + os.path.join(WorkingDirectory, FiltersList))
for x in os.listdir(os.path.join(WorkingDirectory, FiltersList)):
    print(x)
deleting = input("In order to continue we may need to remove the files, you want to remove em?yes/no: ")
if deleting.lower()== "yes":
    for x in os.listdir(os.path.join(WorkingDirectory, FiltersList)):
        os.remove(x)
        print(x + " removed")
else:
    print("No files were delted")
    print("Process stopped")
    sys.exit()


#For column in df we are looking at , we will select those values from our unique list, from those we create NEW data frame out of the SourceFile/Will Be reading file,
#If it starts with its own value will retain it, othwerwise will drop it
#This process only applies once per value due to the list.append  we got, basically at the end of the process we add the variable to a list, and each time rolls up again, 
#it will check if this value is within the list, if not  proceed,


for j in Unique_Values_List:
    if j not in some_list:
        df = pandas.read_excel(os.path.join(WorkingDirectory + Will_Be_Reading_File), engine="openpyxl")
        to_delete_list = []
        for t in df["Customer"]:
            if t.startswith(j):
                pass
            else:
                to_delete_list.append(t)
        df = df[~df['Customer'].isin(to_delete_list)]             
        New_Files_Name = j + ".xlsx"
        df.to_excel(New_Files_Name, index= False, engine= "openpyxl")
        print(t + " has been created")
        some_list.append(j)
print("done")
print(os.path.join(WorkingDirectory, FiltersList))



#H///////////////////////////////////////////////////////
#////////////////////////////////////////////////////////
