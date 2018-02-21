# added a comment to test git hub

def cal_days_diff(a,b):

from datetime import datetime
date_format = "%d/%m/%Y"
d0 = datetime.strptime(a, date_format)
d1 = datetime.strptime(b, date_format)
delta = d0 - d1
return delta



