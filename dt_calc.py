import sys
from datetime import timedelta, datetime as dt

today = dt.now()
print(f'Current date: {today.strftime("%A______%B %d, %Y. %I:%M%p")}') 
def addDay():
      add_days = int(input("how many days will you like to add: "))
      future_day = today + timedelta(days= add_days)
      print(f'Future Date :{future_day.strftime("%A______%B %d, %Y. %I:%M%p")}')
def addWeek():
      add_week = int(input("how many weeks will you like to add: "))
      future_week = today + timedelta(days= add_week * 7)
      print(f'Future Date :{future_week.strftime("%A______%B %d, %Y. %I:%M%p")}')
def addMonth():
      add_month = int(input("how many months will you like to add: "))
      future_month = today + timedelta(days= add_month * 31)
      print(f'Future Date :{future_month.strftime("%A______%B %d, %Y. %I:%M%p")}')    
def addYear():
      add_year = int(input("how many years will you like to add: "))
      future_year = today + timedelta(days= add_year * 365)
      print(f'Future Date :{future_year.strftime("%A______%B %d, %Y. %I:%M%p")}')
def main():
 while True:
        print('''Welcome to future datetime calculator
          
              1.To add days
              2. To add weeks
              3.  To add months
              4.   To add year
              5.    Exit
        
        ''')
        choice = input("Choose from the above:)") 
        if choice == "1":
             print(f'Current date: {today.strftime("%A______%B %d, %Y. %I:%M%p")}')
             addDay()
        elif choice == "2":
             print(f'Current date: {today.strftime("%A______%B %d, %Y. %I:%M%p")}')
             addWeek()
        elif choice == "3":
             print(f'Current date: {today.strftime("%A______%B %d, %Y. %I:%M%p")}')
             addMonth()
        elif choice == "4":
             print(f'Current date: {today.strftime("%A______%B %d, %Y. %I:%M%p")}')
             addYear()
        elif choice == "5":
             sys.exit('Exitted')
        else:
          print(f'Invalid input, choose from 1-5') 
main()  