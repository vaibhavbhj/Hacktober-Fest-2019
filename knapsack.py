
#-------------------Recursive Knapsack-------------------------

def knapSack(W, wt, val, n):
	if(n==0 or W==0):
		return 0
	if(wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))

#--------------------------------------------------------------

def knapSackDP(W, wt, val, n):

	k = [[0 for j in range(W+1)] for i in range(n+1)]

	for i in range(n+1):
		for j in range(W+1):
			if(i==0 or j==0):
				k[i][j] = 0
			elif(wt[i-1] <= W):
				k[i][j] = max(val[i-1] + k[i-1][j-wt[i-1]], k[i-1][j])
			else:
				k[i][j] = k[i-1][j]

	return k[n][W]



val = [60,100,120]
wt =[10,20,30]

W = 50
n = len(val)
print(knapSackDP(W,wt,val,n))
print(knapSack(W, wt, val, n))

