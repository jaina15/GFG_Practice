#User function Template for python3
class Solution:
	def isPalindrome(self, s):
		# code here
        l,r=0,len(s)-1
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return 0
        return 1
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends