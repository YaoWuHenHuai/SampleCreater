import os
import pandas
import win32com.client as win32
from pathlib import Path
import sys

###
Working_Directory = (r"C:\Users\杜甫\Desktop\BaseQueryStructure\\")
Distribution_List_Folder = (r"C:\Users\杜甫\Desktop\Projects\ReportsAutomation\Distribution_List\\")
Distribution_List_File = "Distribution_List.xlsx"
email_list = pandas.read_excel(os.path.join(Distribution_List_Folder, Distribution_List_File), sheet_name="A")
ATTACHMENT_DIR = os.path.join(r"C:\Users\杜甫\Desktop\BaseQueryStructure\\",  "Customers")


first_step = input("Emails will be send, proceed?yes/no:")
if first_step.lower()== "yes":

    outlook = win32.Dispatch("outlook.application")
    os.chdir(Working_Directory)
    ATTACHMENT_DIR = os.path.join(r"C:\Users\杜甫\Desktop\BaseQueryStructure\\",  "Customers")
    for index, row in email_list.iterrows():
        print(row)
        #will get that path from the EMAILs list file, d
        attachment_path = os.path.join(ATTACHMENT_DIR, f"{row['Customer']}.xlsx")
        print(attachment_path)
        #this variable works just the same and fine if siwtch with attachment_path
        Customer_in_file = row['Customer'] + ".xlsx"
        Customer_in_file_path = os.path.join(ATTACHMENT_DIR, Customer_in_file)

        #Only if the customers file exists , 
        if os.path.exists(os.path.join(ATTACHMENT_DIR, f"{row['Customer']}.xlsx")):
            mail = outlook.CreateItem(0)
            mail.To = row["Emails"]
            mail.CC = row["CC"]
            mail.Subject = f"Schedule Update//{row['Customer']}"
            mail.HTMLBody = f"""<p>Good morning {row['Customer']}</p>
                                <p>&nbsp;Maecenas elementum justo lorem, a imperdiet lacus iaculis quis. Mauris venenatis consequat arcu quis mollis. Suspendisse potenti. Donec sagittis elit lorem, porta fringilla lorem rutrum in.</p>
                                <p>&nbsp;Fusce vestibulum aliquet dignissim:</p>
                                <ol>
                                <li><u>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</u></li>
                                <li><u>Pellentesque auctor erat ac efficitur commodo(sed metus)</u></li>
                                <li><u>Praesent commodo ligula turpis, non tristique lectus rhoncus a.</u></li>
                                <li><u>Duis semper arcu a eros pulvinar, quis vestibulum sapien (cursus)</u></li>
                                <li><u>Aliquam sed aliquet ante, ut fermentum tellus.</u></li>
                                <li><u>ivamus feugiat fermentum sem elementum bibendum</u></li>
                                </ol>
                                <p>-</p>
                                <p>Donec malesuada semper ipsum, sed euismod nisi pretium in. Morbi eget iaculis purus. Pellentesque aliquam, risus vulputate gravida dapibus, arcu purus volutpat nibh, eget sollicitudin augue urna ut neque. Aliquam condimentum mollis urna, mattis varius ante finibus malesuada.</p>
                                <p>Anyting you need please get in touch,</p>
                                <p>Greetings,</p>
                                <p><strong>&nbsp;</strong></p>
                                <p><strong>J.Santiago Velazquez G. |&nbsp;</strong></p>
                                <p>&nbsp;</p>
                                <p>Office: 312-494-1725 ext: 4583</p>
                                <p>Direct: 872-268-4583</p>
                                """
            mail.Attachments.Add(Source= attachment_path)
            mail.Display()
            #mail.Send()
    print("Done")
else:
    print("process cancelled")
    sys.exit()
