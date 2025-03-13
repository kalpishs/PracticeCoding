"""Two Sum – Pair with given Sum
https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/

better but not best is sort and do kinda 2 pointer approach O(NlogN)
#https://ide.geeksforgeeks.org/w4H8LiSoYV
#code
def find_pair(num,a,l,r):
    a.sort()
    while l<r :
        if a[l]+a[r]==num:
            #print("Yes")
            return True
        elif a[l] + a[r] < num :
            l += 1
        else:
            r -= 1
    return False

if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        N,X = list(map(int,input().split()))
        #print(T)
        #print(N,X)
        arr = [int(x) for x in input().split()]
        #print(arr)
        if find_pair(X,arr,0,N-1):
            print("Yes")
        else:
            print("No")

"""

#User function Template for python3
class Solution:
    @staticmethod
    def twoSum(arr, target):
        s=set()
        for num in arr:
            couple = target - num
            if couple in s:
                return True
            s.add(num)
        return False
        # code here
