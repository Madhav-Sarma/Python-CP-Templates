import sys
input = sys.stdin.readline

def build(node, low, high):
    if high == low:
        tree[node] = arr[low]
        return
    mid = (low + high) // 2
    build(2*node + 1, low, mid)
    build(2*node + 2, mid + 1, high)
    
    # according to the question here finding max in range
    tree[node] = max(tree[2*node + 1], tree[2*node + 2])


def query(node, low, high, l, r):
    # complete overlaping
    if low >= l and high <= r:
        return tree[node]
    # nothing in common
    if high < l or low > r:
        return float('-inf')  # change this according to the question

    # partial overlaping
    mid = (low + high) // 2
    left = query(2*node + 1, low, mid, l, r)
    right = query(2*node + 2, mid + 1, high, l, r)

    # according to the question here finding max in range
    return max(left, right)


# updating single index of array
def pointUpdate(node, low, high, idx, val):
    if low == high:
        tree[node] = val
        return
    mid = (low + high) // 2
    if idx <= mid:
        pointUpdate(2*node + 1, low, mid, idx, val)
    else:
        pointUpdate(2*node + 2, mid + 1, high, idx, val)

    tree[node] = max(tree[2*node + 1], tree[2*node + 2])


def complete_overlap(l, r, low, high):
    return low >= l and high <= r


# range Update
def rangeUpdate(node, low, high, l, r, val):

    # check pending lazy updates first
    if lazy[node] != 0:
        tree[node] += lazy[node]           # apply the pending value
        if low != high:                    # not a leaf
            lazy[2*node + 1] += lazy[node]
            lazy[2*node + 2] += lazy[node]
        lazy[node] = 0                     # clear lazy

    # no overlapping
    if high < l or low > r:
        return

    # complete overlap
    if complete_overlap(l, r, low, high):
        tree[node] += val
        if low != high:
            lazy[2*node + 1] += val
            lazy[2*node + 2] += val
        return

    # partial overlap
    mid = (low + high) // 2
    rangeUpdate(2*node + 1, low, mid, l, r, val)
    rangeUpdate(2*node + 2, mid + 1, high, l, r, val)
    tree[node] = max(tree[2*node + 1], tree[2*node + 2])


# ---------------------------
# EXAMPLE RUN
# ---------------------------

arr = [1, 2, 3, 4, 5]
n = len(arr)

# if n is the length of the array given tree size at max is 4*n
tree = [0] * (4 * n)
lazy = [0] * (4 * n)

build(0, 0, n - 1)

print("max in range [0,4] =", query(0, 0, n - 1, 0, 4))    # 5

pointUpdate(0, 0, n - 1, 2, 10)
print("after updating index 2 to 10, max =", query(0, 0, n - 1, 0, 4))  # 10

rangeUpdate(0, 0, n - 1, 1, 3, 3)
print("after adding +3 to range [1,3], max =", query(0, 0, n - 1, 0, 4))  # 13
