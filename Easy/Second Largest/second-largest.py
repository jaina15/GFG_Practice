#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		first,second = -1,-1
		for x in arr:
		    if x>first:
		        second = first
		        first = x
		    elif x>second and x!=first:
		        second=x
        return second


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends