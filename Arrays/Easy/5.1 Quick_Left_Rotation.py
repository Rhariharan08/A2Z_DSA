# Problem Link -> https://practice.geeksforgeeks.org/problems/quick-left-rotation3806/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=quick-left-rotation
class Solution:
    def leftRotate(self, arr, k, n):
        k = k % n
        l1 = arr[0:k]
        l2 = arr[k:]
        for i in l1:
            l2.append(i)
        for i in range(0,len(l2)):
            arr[i] = l2[i]
#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        l=list(map(int,input().split()))
        n=l[0]
        k=l[1]
        a = list(map(int,input().split()))
        ob = Solution()
        ob.leftRotate(a,k,n)
        print(*a)
# } Driver Code Ends
