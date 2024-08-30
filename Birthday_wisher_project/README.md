# 🎉 Birthday Wisher 🎂

This project is a fun and handy application that automates the process of sending birthday wishes! 🎁

## 🛠️ Project Details:
- **Language Used:** Python 🐍
- **Libraries Used:** Pandas, smtplib, datetime
- **Description:** 
  - Reads from a `birthdays.csv` file to get the list of birthdays.
  - Checks if today matches any birthday in the file.
  - If there’s a match, it picks a random letter template from the `letter_templates` folder, personalizes it by replacing the `[NAME]` placeholder with the actual name, and sends the birthday wish to the person via email. 📧
  
## 🗂️ How It Works:
1. **Update the CSV:** Add your friends' names, emails, and birthdates in `birthdays.csv`.
2. **Automated Check:** The script checks the current date.
3. **Personalized Wishes:** If today’s someone’s birthday, a personalized email is sent automatically. 🥳

### Happy Wishing! 🎈🎉
