from datetime import datetime, timedelta

today=datetime.now()
yesterday=today-timedelta(1)
tommorow=today+timedelta(1)
print("Yesterday: ", yesterday.strftime('%d-%m-%Y'))
print("Today: ", today.strftime('%d-%m-%Y'))
print("Tommorow: ", tommorow.strftime('%d-%m-%Y'))