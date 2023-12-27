class Solution:
    def thirdLargest(self,a, n):
        first,second,third=-1,-1,-1
        for i in range(n):
            if arr[i]>first:
                third = second
                second = first
                first = arr[i]
            elif arr[i]>second and arr[i]!=first:
                third = second
                second = arr[i]
            elif arr[i]>third and arr[i]!=second:
                third = arr[i]
        return third

#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr, n))
# } Driver Code Ends