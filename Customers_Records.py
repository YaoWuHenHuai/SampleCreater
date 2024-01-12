import os 
import pandas
from datetime import datetime
import numpy
from datetime import date


WorkingDirectory = (r"C:\Users\杜甫\Desktop\BaseQueryStructure\\")
Data_Directory = (r"C:\Users\杜甫\Desktop\Projects\ReportsAutomation\\")
Clients_Records_csv_File = "Customers_Records.csv"
Clients_Records_Excel_File = "Customers_Records.xlsx"
Clients_Records_Dir = os.path.join(WorkingDirectory, "Customers_Records")
TodaysDate = date.today()
TodaysDate = TodaysDate.strftime("%m/%d/%Y")


#Get customers_lists from records
os.chdir(Data_Directory)
reading_df = pandas.read_csv("lists.csv")
Unique_Values_List = []
for x in reading_df["Column"]:
    Unique_Values_List.append(x)



#Case there is no dir, we create it. 
if not os.path.exists(Clients_Records_Dir): 
    os.mkdir(Clients_Records_Dir)
    print(Clients_Records_Dir + " Created")
os.chdir(Clients_Records_Dir)



if os.path.exists(os.path.join(Clients_Records_Dir, Clients_Records_Excel_File)):
    print(Clients_Records_Excel_File + " Do exist")
    Customer_Record_df = pandas.read_excel(Clients_Records_Excel_File)
    print("reading "+ Clients_Records_Excel_File)
    
else:
    print(TodaysDate)
    Dictionary = {"Date":[TodaysDate]}
    Customer_Record_df = pandas.DataFrame(Dictionary)
    print(Customer_Record_df)

#Here we will make a directory out fo the distribution list part.
Distribution_List_Folder = (r"C:\Users\杜甫\Desktop\Projects\ReportsAutomation\Distribution_List\\")
Distribution_List_File = "Distribution_List.xlsx"
os.chdir(Distribution_List_Folder)
email_list = pandas.read_excel(os.path.join(Distribution_List_Folder, Distribution_List_File), sheet_name="A")
customers_list = []
Customers_list_df = pandas.read_excel(os.path.join(Distribution_List_Folder, Distribution_List_File))
for index in email_list.iterrows():
    print(index)
for x in Customers_list_df["Customer"]:
    print(x)
    customers_list.append(x) 
print(customers_list)


#we add customer columns header case they dont exist, we verify from Distribution LIST.xlsx

for x in customers_list:
    if x not in Customer_Record_df.columns:
        Customer_Record_df.insert(1, x, [""])
print(Customer_Record_df)

#
os.chdir(Clients_Records_Dir)


#We iterraw specific column with todaysdata, so within there we notice for each customer didnt update information,.
for index, row in Customer_Record_df.iterrows():
    if row['Date'] == TodaysDate:
        for column, value in row.items():
            print(f"{column}: {value}")
            if column in customers_list:
                if column in Unique_Values_List:
                    Customer_Record_df.at[index, column] = "Did not update on time"
                    print("is there")
                    print(value)
                else:
                    Customer_Record_df.at[index, column] = "Did update on time"


Customer_Record_df.to_csv(Clients_Records_csv_File, index= False)
Customer_Record_df.to_excel(Clients_Records_Excel_File, index= False)
print(TodaysDate)