#User function Template for python3
#problem link -> https://practice.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=check-if-an-array-is-sorted
class Solution:
    def arraySortedOrNot(self, arr, n):
        count2 =1
        for i in range(1,n):
            if arr[i-1] > arr[i]:
                 return 0
            else:
                count2 += 1
        if  count2 == n:
            return 1
           

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        
        ob = Solution()
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends
