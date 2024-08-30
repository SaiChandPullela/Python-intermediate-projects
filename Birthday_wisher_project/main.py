##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import pandas as pd
import random
import smtplib
import datetime as dt


# Getting hold of values in the birthdays.csv file
file = pd.read_csv('birthdays.csv')
names = ', '.join(file['name'].tolist())
mails = ', '.join(file['email'].tolist())
birth_months = file['month'].astype(int).tolist()
birth_days = file['day'].astype(int).tolist()

birthday_names=[]
birthday_mails=[]

# Getting hold of current day and month
now = dt.datetime.now()
for index, row in file.iterrows():
    if row['month'] == now.month and row['day'] == now.day:
        birthday_names.append(row['name'])
        birthday_mails.append(row['email'])

for name in birthday_names:
# Opening the random letter file and replacing the [NAME] placeholder with the name of birthday boy/girl
    with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as letter_file:
        letter = letter_file.read()
        new_letter = letter.replace('[NAME]', name)

    # Getting hold of current day and month
    my_email = 'saichandpullela@gmail.com'
    password = 'jpaz pqpa syvd jxgx'

    # Checking if today is the birthday and if so send the wishes to the person using the smtplib
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_mails[birthday_names.index(name)],
                                msg=f'Subject:Happy Birthday\n\n {new_letter}')





