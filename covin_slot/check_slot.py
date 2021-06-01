'''
import requests
import datetime
import json
import pandas as pd

DIST_ID = 392 # Thane
# DIST_ID = 395 # Mumbai
# DIST_ID = 706 #Pithoragarh

# Print available centre description (y/n)?
print_flag = 'y'

numdays = 10
age = 30
base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]
'''
from typing import Dict
'''
from cowin_api import CoWinAPI

cowin = CoWinAPI()

states = cowin.get_states()
#print(states) for state #29 for Raj
state_id = '29'
cowin = CoWinAPI()
districts = cowin.get_districts(state_id)
#print(districts)    #505 for jaipur I , 506 for jaipur II


date = '13-05-2021'  # Optional. Takes today's date by default
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
district_id = '512'
cowin = CoWinAPI()
available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
'''
#print(available_centers)
import requests
import json
import datetime
import time
import AppKit

list_of_date_time=[]
now= datetime.datetime.now()
for i in range(0,2):
    list_of_date_time.append((now+datetime.timedelta(days=i)).strftime("%d-%m-%Y"))
headers = {'accept': 'application/json','User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
bas_url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict"
district_id = '505'
try_count=0
print_flag=0
while True:
    for date in list_of_date_time:
        params = {'district_id': district_id, 'date': date}
        try:
            response = requests.get(bas_url,params=params,headers=headers)
        except Exception as ex:
            print(f"{ex}")
        try:
            json_res=response.json()
        except  Exception as ex:
            print(f"got exeception {ex}")
            time.sleep(3)
            json_res=json.loads('''{"sessions": []}''')
        length= len(json_res['sessions'])
        list_centers=[]
        if length >0:
            for center in json_res['sessions']:
                center_id=center['center_id']
                center_name=center['name']
                pincode=center['pincode']
                address=center['address']
                fee=center['fee_type']
                date=center['date']
                available_slot=center['available_capacity']
                age=center['min_age_limit']
                vaccine_type=center['vaccine']
                res_text=f"pin: {pincode} - Slot: {available_slot} at : {center_name} for age: {age} " \
                         f"on {date}. Vaccine available is {vaccine_type}."
                if fee !='0' and fee!='Free':
                    res_text+=f"It will cost you {fee}."
                else:
                    res_text += f"it will be free of cost for you."
                if address != '':
                    res_text=res_text+f"also address of center is {address}\n"
                list_centers.append((res_text,(age,available_slot)))
            for res in list_centers:
                if int(res[1][0]) != 45 and int(res[1][1]) != 0:
                    print_flag=1
                    print(res[0])
                elif  int(res[1][0]) == 45 and int(res[1][1]) != 0:
                    print(f"JUST FYI {res[0]}")
                buzz = 10000
                while buzz > 0:
                    if int(res[1][0]) != 45 and int(res[1][1]) !=0:
                     AppKit.NSBeep()
                    else:
                        break
                    buzz -= 1
                buzz= 10000
    if print_flag!=1:
        try_count+=1
        print(f"No Slot try count:{try_count}")
    else:
        print_flag=0
    time.sleep(3)