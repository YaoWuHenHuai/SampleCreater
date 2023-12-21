
import os

#人不可貌相， 海水不可斗量
#READ
#Uptade Files by removing and grabing from new file sources
#1. DELETE OLD FILES in (ToUpdateDirecry)
#2. GET NEW ONES, COPY or Generate Em

ToUpdateDirectory = (r"C:\Users\杜甫\Desktop\BaseQueryStructure\\")
os.chdir(ToUpdateDirectory)

def remove_file(x):
    print("Deleting File " + x)
    os.remove(ToUpdateDirectory + x)
    print("Deleted" + x)

for x in os.listdir(ToUpdateDirectory):
    if x.startswith("AceptanceReport"):
        remove_file(x)
    if x.startswith("AllOperationData"):
        remove_file(x)  
    if x.startswith("PerformanceReport"):
        remove_file(x)
    if x.startswith("TimelyUpdates"):
        remove_file(x)
