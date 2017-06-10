from datetime import date, datetime

try:
    date_string = input("Give you DY.MN.YEAR of birthday (ex. 01.01.1980): ")
    date_dt = datetime.strptime(date_string, '%d.%m.%Y')
    print(date_dt.strftime('%A %d.%m.%Y'))
except ValueError:
    print("\nSorry! Check the input format.")
