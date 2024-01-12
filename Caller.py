import os
import sys

WorkingDirectory = (r"C:\Users\杜甫\Desktop\Projects\ReportsAutomation")
os.chdir(WorkingDirectory)


query=input("Which query to run? Customers_Records/Filtering_Customers/Emails_Sender/Samples_Creater/UpdateFiles: ") 
if query.lower()=="customers_records": 
	os.system("python Customers_Records.py") 

elif query.lower()=="filtering_customers":
	os.system("python Filtering_customers.py")

elif query.lower()=="emails_sender":
	os.system("python emails_sender.py") 

elif query.lower()=="updatefiles":
	os.system("python Updatefiles.py") 

elif query.lower()=="samples_creater":
	os.system("python Samples_Creater.py") 

else: 
	sys.exit() 

