from typing import *

class BinarySearch():
    def binary_search(self,arr: List[int],low:int,high:int,x:int,count):
        if high >= low:
            mid = low + (high-low)//2
            count += 1
            if arr[mid]==x:
                return mid,count
            if arr[mid] > x:
                return self.binary_search(arr,low,mid-1,x,count)
            else:
                return self.binary_search(arr,mid+1,high,x,count)
        else:
            return -1,count


if __name__ =="__main__":
    bS = BinarySearch()
    inputArr = [2, 3, 4, 10, 40]
    searchElem = 2
    low=0
    high=len(inputArr)-1
    result,count=bS.binary_search(inputArr,low,high,searchElem,0)
    if result != -1:
        print(f"Element {searchElem} found at index {result} after {count} iterations.")
    else:
        print(f"Element {searchElem} not found after {count} iterations, so index is {result}")
