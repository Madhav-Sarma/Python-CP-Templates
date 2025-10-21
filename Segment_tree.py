def build(node,low,high):
    if high==low:
        tree[node]=arr[low]
        return
    mid=(low+high)//2
    build(2*node+1,low,mid)
    build(2*node+2,mid+1,high)
    
    #according to the question here finding max in range
    tree[node]=max(tree[2*node+2],tree[2*node+1])


def query(node,low,high,l,r):
    #complete overlaping
    if low>=l and high<=r:
        return tree[node]
    #nothing in common
    if high<l or low>r:
        return float('-inf')
    #partial overlaping
    mid=(low+high)//2
    left=query(2*node+1,low,mid,l,r)
    right=query(2*node+2,mid+1,right,l,r)

    #according to the question here finding max in range
    return max(left,right)


arr=[1,2,3,4,5]
n=len(arr)
#if n is the lenght of the array given tree size at max is 4*n
tree=[0]*(4*n)
