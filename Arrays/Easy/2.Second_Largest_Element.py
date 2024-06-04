#User function Template for python3
#Problem Link -> https://practice.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest
class Solution:

	def print2largest(self,arr, n):
		a = arr[0]
		s = -1
		for i in range(1,n):
		    if arr[i] > a:
		        a = arr[i]
		        
		for i in range(0,n):
		    if s < arr[i] and arr[i] != a:
		        s = arr[i]
		return s


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
