import json
from queue import Empty
from turtle import pd
from unittest import result
import requests
from datetime import datetime
from datetime import datetime
import datetime
from datetime import date
import calendar
# Import smtplib for the actual sending function
import smtplib

# Send Email code
from email.message import EmailMessage
def send_mail(to_email, subject, message, server='smtp.example.cn',
              from_email='xx@example.com'):
    # import smtplib
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg.set_content(message)
    print(msg)
    server = smtplib.SMTP(server)
    server.set_debuglevel(1)
    server.login(from_email, 'password')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')

# load Api
api_response = requests.get('https://interview-assessment-1.realmdigital.co.za/employees')
data = api_response.text
parse_json = json.loads(data)

# current date and time
today = date.today().strftime('%d-%m') 

#birthday wishes message
message = "Happy Birthday"

# load api function
def main_request():
    parse_json = json.loads(data)
    return parse_json

# Function to call all data
all_results = main_request()

#Fuction to display bithday attribute
def date_of_birth():
    for birthday_data in all_results:
        # loop for birthday attribute
        dateOfBirth = birthday_data['dateOfBirth']
        #Last notification
        notification = birthday_data['lastNotification']
        # emp active or not
        emp_active = datetime.datetime.strptime(notification, "%Y-%m-%d")
        biemp_active_confirm = emp_active.strftime("%y")

        # date convert
        emp_birth_day =  datetime.datetime.strptime(dateOfBirth, "%Y-%m-%dT00:00:00")
        # date format
        birthday = emp_birth_day.strftime("%d-%m")
        #condition: if a date is equal to the employee birthday then retun true

        # leap year 
        year = date.today().strftime('%y') 
        is_leap_year = calendar.isleap(year)

        # if is employee birthday then send email
        if birthday == today:
            send_mail(to_email=['12345@qq.com', '12345@126.com'], subject='Birth day Wishes', message='Happy Birth dat' + birthday_data['name'])
          
        #if not a leap year the below condition will accomodate the 29th of Feb Day
        elif not is_leap_year:
            if birthday == '29-02':
                # Leap condition

                ######## Big note, the app will not send the employee email dynamic because there is no email attribute in an API
                send_mail(to_email=['12345@qq.com', '12345@126.com'], subject='Birth day Wishes', message='Happy Birth dat' + birthday_data['name'])
        # notification for in active employee
        elif not biemp_active_confirm ==  '2021' and not biemp_active_confirm == "":
            print ('Employee no longer working for RealM Digital')
        
        elif biemp_active_confirm == "":
            print ("The employee has not started working for RealM Digital")
        else:
            print ('no birth day today')
            break
    return ("200")

# function to call date of birth data
empDateOfBirth = date_of_birth()



