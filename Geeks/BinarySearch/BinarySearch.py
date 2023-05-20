from typing import *


class BinarySearch:
    def myBinarySearch(self, input: List[int], search: int, low: int, high: int):
        if high >= low:
            mid = low + (high-low)//2
            # If element is present at the middle itself

            if input[mid] == search:
                return mid

            if input[mid] > search :
                return self.myBinarySearch(input,search,low,mid-1)
            else:
                return self.myBinarySearch(input,search,mid+1,high)
        else:
            return -1

    def binarySearch(self, input: List[int], search: int):
        return self.myBinarySearch(input, search, 0, len(input) - 1)


if __name__ =="__main__":
    bS = BinarySearch()
    inputArr = [2, 3, 4, 10, 40]
    searchElem = 10
    result=bS.binarySearch(inputArr,searchElem)
    if result != -1:
        print("Element is present at index % d" % result)
    else:
        print("Element is not present in array")
