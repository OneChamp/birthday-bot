##################### Extra Hard Starting Project ######################
import datetime as dt
from dataclasses import replace

import pandas
import smtplib
from email.message import EmailMessage
import random

cur_year=dt.datetime.now().year
cur_month=dt.datetime.now().month
cur_day=dt.datetime.now().day
cur_weekday=dt.datetime.now().weekday
username = "brucewayne78602@gmail.com"
# noinspection SpellCheckingInspection
password = "uoxvlqectvzoxhnt"
birthdate_to_dict=[]
template_list=["letter_1.txt","letter_2.txt","letter_3.txt","letter_4.txt","letter_5.txt",
               "letter_6.txt","letter_7.txt","letter_8.txt","letter_9.txt","letter_10.txt"]
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
def send_email(usr_email,usr_name):
    msg=EmailMessage()
    msg["From"]=username
    msg["To"]=usr_email
    sending_template=random.choice(template_list)
    print(sending_template)
    try:
        with open(f"letter_templates/{sending_template}","r") as f:
             em_temp=f.read()
             final_temp=em_temp.replace("[NAME]",usr_name)
             msg.set_payload(final_temp)
    except FileNotFoundError:
        print("File not found!")
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com',465,timeout=10) as connection:
            connection.login(user=username, password=password)
            connection.send_message(msg)
            print("Email sent!")
    except Exception as e:
            print("Email not sent",e)

try:
    birthdate_data=pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("No  file found!")
else:
    birthdate_to_dict=birthdate_data.to_dict(orient="records")

if birthdate_to_dict is not None:
    for birthdate in birthdate_to_dict:
         if birthdate["day"]==cur_day and birthdate["month"]==cur_month:
             user_email=birthdate["email"]
             user_name=birthdate["name"]
             send_email(user_email,user_name)


