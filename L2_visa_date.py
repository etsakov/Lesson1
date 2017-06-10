from datetime import date, datetime, timedelta

date_string = input("insert date as 25.12.2017: ")

length_of_stay = int(input("how many days to stay in Schengen? "))

date_str = datetime.strptime(date_string, '%d.%m.%Y')

delta = timedelta(days=length_of_stay)

return_date = date_str + delta 
print("you'll return on ", return_date.strftime('%A %d.%m.%Y'))


