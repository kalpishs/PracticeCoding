from datetime import datetime, timedelta
inputdate="20220228"
datetime_object = datetime.strptime(inputdate, '%Y%m%d')
res=datetime_object  + timedelta(days=1)
print("\"pay.analytics.job.runDate\":\""+res.strftime("%Y%m%d")+"\",")