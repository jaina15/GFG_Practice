#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr, n):
		# code here
		x=0
		for i in range(n):
		    if arr[i]%2==0:
		        arr[x],arr[i]=arr[i],arr[x]
		        x+=1
		
		for i in range(n):
		    if arr[i]%2!=0:
		        break
		
		arr[:i]=sorted(arr[:i])
		arr[i:]=sorted(arr[i:])


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends