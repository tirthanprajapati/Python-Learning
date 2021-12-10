import pytz
import datetime
import time

home=pytz.timezone('Asia/Kolkata')
local_time=datetime.datetime.now(home)
current_time=local_time.strftime("%H:%M:%S")
print(current_time)
