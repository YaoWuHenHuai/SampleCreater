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

print("The following are the current files within the MainDirectory:")
list = []
for x in os.listdir(MainDirectory):
    list.append(x)
    #print(x)
for x in enumerate(list):
    print(x)

#Will each document at the directory  will create sample data information
for x in os.listdir(MainDirectory):
    if os.path.exists(os.path.join(MainDirectory, x)):
        print(x + " will be read")
        df = pandas.read_excel(x)
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
        for _ in range(1000):
            SampleCreator(df, today, CustomersList,conteo)

        print(df)
        print(df.tail(1))
        df.to_excel(x, index=False)
        end = timer()

        print(end - start)        
