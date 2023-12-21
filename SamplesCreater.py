import os 
import pandas
import datetime
from datetime import date
import numpy
import random
from timeit import default_timer as timer



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
file_name = "AceptanceReport.xlsx"
file_path = os.path.join(MainDirectory, file_name)
if os.path.exists(os.path.join(file_path)):
    print("already there")
else:
    create_empty_dataframe(file_path)


file_name = "AllOperationData.xlsx"
file_path = os.path.join(MainDirectory, file_name)
if os.path.exists(os.path.join(file_path)):
    print("already there")
else:
    create_empty_dataframe(file_path)


file_name = "PerformanceReport.xlsx"
file_path = os.path.join(MainDirectory, file_name)
if os.path.exists(os.path.join(file_path)):
    print("already there")
else:
    create_empty_dataframe(file_path)

file_name = "TimelyUpdates.xlsx"
file_path = os.path.join(MainDirectory, file_name)
if os.path.exists(os.path.join(file_path)):
    print("already there")
else:
    create_empty_dataframe(file_path)



print("The following are the current files within the MainDirectory:")
list = []
for x in os.listdir(MainDirectory):
    list.append(x)
    #print(x)
for x in enumerate(list):
    print(x)

#Will each document at the directory  will add sample information within the files that are in there 
for x in os.listdir(MainDirectory):
    #double check
    if os.path.exists(os.path.join(MainDirectory, x)):
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
            df.loc[len(df)] = new_row_data
        #How many rows of sample we want, in this case its 1000,
        for _ in range(1000):
            SampleCreator(df, today, CustomersList,conteo)

        print(df)
        print(df.tail(1))
        df.to_excel(x, index=False)
        end = timer()

        print(end - start)  
        print(end - start)        
