# cook your dish here
n,m=map(int,input().split())
a=[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    k=list(map(int,input().split()))
    for j in range(1,m+1):
        a[i][j]=a[i-1][j]+a[i][j-1]-a[i-1][j-1]+k[j-1]
print(a)

#a[i][j] is the prefix sum till i,j
#query of sum can be done in O(1) after precomputing this prefix sum
#made easy for matrix

###how??
#like so:
'''
for k in range(int(input())):
    x1,y1,x2,y2=map(int,input().split())
    print(a[x1-1][y1-1]+a[x2][y2]-a[x1-1][y2]-a[x2][y1-1])
'''

##draw abox to understand how it works