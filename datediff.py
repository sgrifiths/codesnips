# added a comment to test git hub
from datetime import datetime

def cal_days_diff(a,b,date_format):
    d0 = datetime.strptime(a, date_format)
    d1 = datetime.strptime(b, date_format)
    delta = d0 - d1
    return delta



