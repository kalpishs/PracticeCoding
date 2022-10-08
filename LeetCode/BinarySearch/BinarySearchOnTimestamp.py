"""
981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Date : 06-oct-2022
"""
from typing import *


class TimeMap:

    def __init__(self):
        self.store = {}  # key, List[Value,Timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[value, timestamp]]
        else:
            self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
                pass
            else:
                r = mid - 1
                pass
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ =="__main__":
    timeMap = TimeMap()
    res=[]
    res.append(timeMap.set("foo", "bar", 1))#store the key "foo" and value "bar" along with timestamp = 1.
    res.append(timeMap.get("foo", 1)) # return "bar"
    res.append(timeMap.get("foo", 3))
    """return "bar", since there is no value corresponding to foo at 
     timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar"."""
    res.append(timeMap.set("foo", "bar2", 4) ) #store the key "foo" and value "bar2" along with timestamp = 4.
    res.append(timeMap.get("foo", 4)) #return "bar2"
    res.append(timeMap.get("foo", 5)) #return "bar2"
    print(res)
    #Output: "[null,"bar","bar",null,"bar2","bar2"]"

