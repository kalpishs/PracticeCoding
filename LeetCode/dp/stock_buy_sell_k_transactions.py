#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""prices=[5, 11, 3, 50, 60, 90]   Max with K=2



buy at 5
sell at 11



buy at 3
sell at 90


Max profit =93

profit_table=

	prices=		5	11	3	50	60	90

		0   	0	0	0	0	0	0

		1	0	6	6	47	57	87

		2	0	6	6	53	63


		for profit_table[2][prices[5]]# output is 93

		#trasaction t on day d


					   	 |
					  	 |  1) profit[t][d-1]=63 #same number of transation on previous day i.e no trnx.
					  	 |
		profit [t][d]=max|
						 |
						 |
						 |	2)  prices[d]=90 #since we sold at day d + max (-ve prices[x]+profit[t-1][x])
						 												0<=x<day


						 												x=0 : -prices[0]+profit[2-1][0]
						 													  -5+0
						 													  -5

						 												x=1: -prices[1]+profit[1][1]
						 													 -11+6= -5

						 												x=2: -prices[2]+profit[1][2]
						 													 -3+6 = 3    	#greatest value
						 												x=3: -prices[3]+profit[1][3]
						 													 -50+47 = -3
						 												x=4: -prices[4]+profit[1][4]
						 													 -60+57 = -3



						 		90       	+ 	3 = 93


	profit_table=

			5	11	3	50	60	90

		0   	0	0	0	0	0	0

		1	0	6	6	47	57	87

		2	0	6	6	53	63	93




		O(n^2 K)



		for profit_table[2][prices[4]] #output is 63


			   	 |
					  	 |  1) profit[t][d-1]=53 #same number of transation on previous day i.e no trnx.
					  	 |
		profit [t][d]=max|
						 |
						 |
						 |	2)  prices[d]=60 #since we sold at day d + max (-ve prices[x]+profit[t-1][x])
						 												0<=x<day


						 												x=0 : -prices[0]+profit[2-1][0]
						 													  -5+0
						 													  -5

						 												x=1: -prices[1]+profit[1][1]
						 													 -11+6= -5

						 												x=2: -prices[2]+profit[1][2]
						 													 -3+6 = 3    	#greatest value
						 												x=3: -prices[3]+profit[1][3]
						 													 -50+47 = -3

"""

import sys
from typing import *
class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		len_prices=len(prices)
		if len_prices==0 or k==0:
			return 0
		if 2 * k > len_prices:
			res = 0
			for i in range(1, len_prices):
				price = prices[i] - prices[i - 1]
				if price > 0:
					res += price
			return res
		profit_dp_table=[[0 for rows in range(len_prices)] for cols in range (k+1)] #majorly for filling 1st row and 1st'
																					# col as 0 since we have max profit as 0 if only 1 tnx is allowed
																					# also 0 profit if we have only 1 price avilable
		for tnx in range(1,k+1):
			maxSoFar=-sys.maxsize-1
			for day in range (1,len_prices):
				maxSoFar=max(maxSoFar,profit_dp_table[tnx-1][day-1] -prices[day-1]) # max profit is always equal max till day 0,1,...day-2 or tnx-1,day-1 -price at day -1
				profit_dp_table[tnx][day]=max(profit_dp_table[tnx][day-1],maxSoFar+prices[day])
			#Time complexity O(tnx*day)
		return profit_dp_table[-1][-1]
		#Time complexity O(tnx*day) | O(tnx*day) space
if __name__=="__main__":
	solve=Solution()
	print(solve.maxProfit(2,[5, 11, 3, 50, 60, 90]))