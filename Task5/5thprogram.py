# Use lambda function to extract the year,month,and day from datetime object
# 1. create datetime function
# 2. using year month day attribute separate from datetime object and print it

from datetime import datetime
time=datetime.now()
year=lambda x:(x.year,x.month,x.day)
print(year(time))
