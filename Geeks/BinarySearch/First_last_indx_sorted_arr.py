
"""
https://www.geeksforgeeks.org/find-first-and-last-positions-of-an-element-in-a-sorted-array/
"""
class BinarySearch:
    def binarySearch(self, arr, x, low, high, findStart):
        if high >= low:
            mid = low + (high - low) // 2
            if arr[mid] == x:
                if findStart:
                    if (mid == 0 or arr[mid - 1] < x):
                        return mid
                    else:
                        return self.binarySearch(arr, x, low, mid - 1, findStart)
                else:
                    if (mid == high or arr[mid+1] > x):
                        return mid
                    else:
                        return self.binarySearch(arr, x, mid + 1,high, findStart)
            elif arr[mid] > x:
                return self.binarySearch(arr, x, low, mid - 1, findStart)
            elif arr[mid] < x:
                return self.binarySearch(arr, x, mid + 1, high, findStart)
        else:
            return -1


# Function for finding first and last occurrence of x
def find(arr, x):
    n = len(arr)
    bs = BinarySearch()
    # return index of first occurrence
    first = bs.binarySearch(arr, x, 0, len(arr) - 1, True)

    # return index of last occurrence
    last = bs.binarySearch(arr, x, 0, len(arr) - 1, False)

    res = [first, last]
    return res


if __name__ == "__main__":
    arr =  [1, 3, 6,7,8,10,11,12,13,15,17,19,19,20,20]
    x = 62
    res = find(arr, x)
    print(res[0], res[1])