from datetime import datetime


value = "29.09.2014"
print(datetime.strptime(value, "%d.%m.%Y"))