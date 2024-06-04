#User function Template for python3
#Problem Link -> https://practice.geeksforgeeks.org/problems/reversal-algorithm5340/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=reversal-algorithm
class Solution:
    def leftRotate(self, arr, n, d):
       l1 = arr[:d]
       l2 = arr[d:]
       for i in l1:
           l2.append(i)
       for i in range(0,len(l2)):
           arr[i] = l2[i]
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        d = int(input())
        ob = Solution()
        ob.leftRotate(arr, n, d)
        for xx in arr:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends
