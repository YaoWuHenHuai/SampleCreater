import os 
import pandas
import datetime
from datetime import date
import numpy
import random
from timeit import default_timer as timer
import sys
import time

start = timer()

#Creating DataForSample
MainDirectory = (r"C:\Users\杜甫\Desktop\BaseQueryStructure")
os.chdir(MainDirectory)
print("Current directory is "+ MainDirectory)

#Databases {AcceptanceReport, AllOperationData, PerformanceReport, TimelyUpdates}

file_name = ""
file_path = os.path.join(MainDirectory, file_name)

#Define Function creates files, 
def create_empty_dataframe(file_path):
    createfiledf = pandas.DataFrame(columns= ["OperationId", "Date", "Customer", "CustomerID",
                    "TransportationCompany", "TransportationCompanyID",
                    "DepartureDate", "DeparturePlace", "ArrivingDate", "ArrivingPlace"],)
    createfiledf.to_excel(file_name, index=False)


#We Review by File name, case it exists pass, else will create file with the according columns 
def file_creater(file_path):
    if os.path.exists(os.path.join(file_path)):
        print(file_name +" already there")
    else:
        print(file_name + " not there, will be created de")
        create_empty_dataframe(file_path)

file_name = "AceptanceReport.xlsx"
file_path = os.path.join(MainDirectory, file_name)
file_creater(file_path)

file_name = "AllOperationData.xlsx"
file_path = os.path.join(MainDirectory, file_name)
file_creater(file_path)

file_name = "PerformanceReport.xlsx"
file_path = os.path.join(MainDirectory, file_name)
file_creater(file_path)

file_name = "TimelyUpdates.xlsx"
file_path = os.path.join(MainDirectory, file_name)
file_creater(file_path)


print("The following are the current files within the MainDirectory:")
list = []
for x in os.listdir(MainDirectory):
    list.append(x)
    #print(x)
for x in enumerate(list):
    print(x)

To_work_files = []
PerformanceReport= "PerformanceReport.xlsx"
AllOperationData= "AllOperationData.xlsx"
AceptanceReport= "AceptanceReport.xlsx"
TimelyUpdates= "TimelyUpdates.xlsx"
To_work_files.append(PerformanceReport)
To_work_files.append(AllOperationData)
To_work_files.append(AceptanceReport)
To_work_files.append(TimelyUpdates)
x_list = []

print("The sample will be made within the following files")
for x in To_work_files:
    print(x)


#We ask the user in case they want to do sample for additional case
BeforeProceding = input("is there any you want to add?yes/no:")
if BeforeProceding.lower()== "yes":
    for x in os.listdir(MainDirectory):
        if x not in To_work_files:
            if x.endswith(".xlsx"):
                print(x)
                if x not in x_list:
                    x_list.append(x)
    for x in x_list:
        print(x)
    counting = 0
    for y in x_list:
        counting += 1    

    if counting == 0:
        print("empty")
        print("cannot proceed, will continue")
        Inform_message=input("empty, so will continue, ok?")
        if Inform_message.lower() == "ok":
            pass
        else:
            pass
    else:
        def asking_thing(To_work_files):
            useless_counting=0
            for z in x_list:
                useless_counting += 1
            if useless_counting>= 1:
                Second_Step= input("The following could be added: " + str(x_list) + "\nWhich one to add or stop?: ")
                for z in x_list:
                    if Second_Step.lower()== z.lower():
                        if z not in To_work_files:
                            To_work_files.append(z)
                            print(z+ "added to " + str(To_work_files) + " list")
                            print("sucessfully added")
                            x_list.remove(z)
                            asking_thing(To_work_files)          
                        else:
                            print(z +" already there")
                            x_list.remove(z)
                            asking_thing(To_work_files)
                    elif Second_Step.lower()== "stop":
                        break
                    else:
                        print("Not valid value detected")
                        asking_thing(To_work_files)
            else:
                print("there is no values within the list left")
                print("will procceed")
                time.sleep(5)     
        asking_thing(To_work_files)
        
    #SecondStep = input("these are the files could be add to the list: "+ x_list)
    #if SecondStep.lower()=="s":
        #print("nice")
else:
    print("all right")
    pass
    
        
    




#Will each document at the directory  will add sample information within the files that are in there 



###Here we will read a header s file, so, if each reading file doesnt match , then it wont proceed, 
header_file = "header.xlsx"
header_df = pandas.read_excel(header_file, engine="openpyxl")
header_values_list= []
for header_values in header_df.columns:
    header_values_list.append(header_values)
    
for x in To_work_files:
    print(x + " will be read")
    df = pandas.read_excel(x, engine="openpyxl")
    print(df)
    column_names = df.columns.values.tolist()
    print(column_names)
    print("done reading")

    today = date.today()
    today = today.strftime("%m/%d/%Y, %H:%M:%S")
    random_number = random.randint(2000,9999)
    random_sample = str(random_number)
    random_number = random.randint(2000,9999)
    CustomersList = ["LocalMarket", "KFC", "PizzaHut"]
    TransportationCompanyList = ["Transportadora Del Norte SA", "Mendoza SA", "Transportes Oscar SA"]
    DeparturePlaceList = ["AreaA", "AreaB", "AreaC", "AreaD"]
    ArrivingPlaceList = ["KFC Sucursal Cumbres", "LittleCeasars Sucursal Leones", "Soriana San Jemo"]
    conteo = [0]
    def SampleCreator(df, today, CustomersList, conteo):
        conteo.append(1)
        #print(sum(conteo))
        print("creating row number " +  str(sum(conteo)))
        new_row_data = {
            "OperationId": random.randint(2000,9999),
            "Date": today,
            "Customer": random.choice(CustomersList),
            "CustomerID": ("C" + str(random.randint(2000, 9999))),
            "TransportationCompany": random.choice(TransportationCompanyList),
            "TransporationCompanyID": ("T" + str(random.randint(2000, 9999))),
            "DepartureDate": today,
            "DeparturePlace": random.choice(DeparturePlaceList),
            "ArrivingDate": today,
            "ArrivingPlace": random.choice(ArrivingPlaceList),
        }
        print(new_row_data)
        if all(z in header_values_list for z in df.columns):
            df.loc[len(df)] = new_row_data

        else:
            print("columns dont match")
            print("sample wont be created")
            time.sleep(2)
    #How many rows of sample we want, in this case its 1000,
    for _ in range(1000):
        SampleCreator(df, today, CustomersList,conteo)

    print(df)
    print(df.tail(1))
    df.to_excel(x, index=False)
    end = timer()

    print(end - start)     

print(To_work_files)


