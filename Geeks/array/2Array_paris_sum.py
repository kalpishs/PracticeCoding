#https://www.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card


class Solution:
    def allPairs(self, target, arr1, arr2):
        dict_d={}
        result=[]
        n=len(arr1)
        m=len(arr2)
        for i in range (0, n):
            dict_d[arr1[i]]=dict_d.get(arr1[i],0)+1
        for j in range(0,m):
            if target-arr2[j] in dict_d:
                my_tuple=(target-arr2[j] ,arr2[j])
                result.extend([my_tuple]*dict_d[target-arr2[j]])
        return sorted(result, key=lambda x: x[0])

        # Your code goes here


if __name__ =="__main__":
    sol = Solution()
    inputArr:list[int] = [2, 3, 4, 10, 40, 30]
    inputArr2:list[int] = [15,45,12,41,44,43,25]
    numberX:int = 55
    result=sol.allPairs(numberX,inputArr,inputArr2)
    print(f"The pairs with Sum {numberX} is {result}")