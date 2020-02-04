import datetime

# print(datetime.datetime.now())


datetime_str = '09/19/18'

datetime_object = datetime.datetime.strptime(datetime_str, '%m/%d/%y')
print(datetime_object)