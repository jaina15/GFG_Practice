#User function Template for python3

class Solution:
    def totalFine(self, n, date, car, fine):
        ans=0
        if date%2==0:
            for i,v in enumerate(car):
                if v%2!=0:
                    ans+=fine[i]
        else:
            for i,v in enumerate(car):
                if v%2==0:
                    ans+=fine[i]
        return ans
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        brr = [int(x) for x in input().strip().split()]
        
        print(Solution().totalFine( n, k, arr, brr))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends