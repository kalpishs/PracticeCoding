#https://www.geeksforgeeks.org/count-pairs-with-given-sum/
class Solution:
    #Complete the below function
    def countPairs(self,arr, target):
        freq= {}
        count=0
        for i in range(len(arr)):
            if (target- arr[i]) in freq:
               count+=freq[target- arr[i]]
            freq[arr[i]]=freq.get(arr[i],0)+1
        return count
        #Your code here


