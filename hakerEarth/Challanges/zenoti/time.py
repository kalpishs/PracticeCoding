import math

from datetime import datetime

def Solve(R,N,P):
    FMT = '%H:%M:%S'
    result_diff=[]
    for i in P:
        delta = datetime.strptime(R, FMT) - datetime.strptime(i, FMT)
        get_sec=delta.seconds
        if (get_sec>=3600):
            hr=int(math.floor(get_sec/3600))
            if hr==1:
                result_diff.append(str(hr)+ ' hour ago' )
            else:
                result_diff.append(str(hr) + ' hours ago')
        elif (get_sec >= 60):
            min=int(math.floor(get_sec / 60))
            if min==1:
                result_diff.append(str(min) + ' minute ago')
            else:
                result_diff.append(str(min) + ' minutes ago')
        elif(get_sec>0):
            if get_sec==1:
                result_diff.append(str(int(math.floor(get_sec))) + ' second ago')
            else:
                result_diff.append(str(int(math.floor(get_sec))) + ' seconds ago')
        else:
            result_diff.append('now')
    return result_diff

R='23:05:38'
P=['23:05:38','23:05:02','23:04:59','23:04:31','12:36:07','08:59:01','00:00:00','23:05:37']
out=Solve(R,2,P)
for in_out in out:
    print(in_out)