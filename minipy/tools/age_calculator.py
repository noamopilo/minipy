from dateutil.relativedelta import relativedelta
from datetime import datetime, date

def calculate_age(birth_date):
    today = date.today()
    
    age = relativedelta(today, birth_date)
    return age.years

        


birth_date_input = input("What is your date of birth? (year/month/day): ")

birth_date = ""

try: 
    birth_date = datetime.strptime(birth_date_input, "%Y/%m/%d").date()
    age = calculate_age(birth_date)
    print(f"Your age is: {age}")
except ValueError:
    print("Please input a valid date in the correct format (year/month/day)")

