#User function Template for python3
#Problem Link -> https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=move-all-zeroes-to-end-of-array
class Solution:
	def pushZerosToEnd(self,arr, n):
    	s = [0] * len(arr)
    	j = 0
    	for i in range(len(arr)):
    	    if arr[i] != 0:
    	        s[j] = arr[i]
    	        j += 1
    	for i in range(len(arr)):
    	    arr[i] = s[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends    	

