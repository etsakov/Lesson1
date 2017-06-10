from datetime import date, datetime, timedelta

dt_today = date.today()
print("Today is ", dt_today)

delta_yesterday = timedelta(days=1)
delta_yesterday

dt_yesterday = dt_today - delta_yesterday

print("Yesterday was ", dt_yesterday)

#There should be a way to make this with month count
delta_month = timedelta(days=30)
delta_month

dt_month = dt_today - delta_month

print("A month ago was ", dt_month)

