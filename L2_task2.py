from datetime import date, datetime, timedelta

date_string = '01/01/17 12:10:03.12345'
date_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
print(date_dt)