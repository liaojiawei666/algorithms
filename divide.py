################################################################################################################
#find_max_crossing_subarray和find_maximum_subarray为寻找数组中增长最大的子数组函数，例如[-1,3,-4,5,2,-4]返回(3,4,7)
def find_max_crossing_subarray(A,low,mid,high):

    left_sum=float('-inf')
    sum=0
    for i in range(mid,low-1,-1):
        sum+=A[i]
        if sum>left_sum:
            left_sum=sum
            left_max=i

    right_sum=float('-inf')
    sum=0
    for i in range(mid+1,high+1):
        sum+=A[i]
        if sum>right_sum:
            right_sum=sum
            right_max=i
    return left_max,right_max,left_sum+right_sum

def find_maximum_subarray(A,low,high):
    if low==high:
        return (low,high,A[low])
    mid=(low+high)//2
    (left_low,left_high,lef_sum)=find_maximum_subarray(A,low,mid)
    (right_low,right_high,right_sum)=find_maximum_subarray(A,mid+1,high)
    (cross_low,cross_high,cross_sum)=find_max_crossing_subarray(A,low,mid,high)
    if lef_sum>=right_sum and lef_sum>=cross_sum:
        return (left_low,left_high,lef_sum)
    elif right_sum>=lef_sum and right_sum>=cross_sum:
        return (right_low,right_high,right_sum)
    else:
        return (cross_low,cross_high,cross_sum)

# def test():
#     A=[-1,3,-4,5,2,-4]
#     print(find_maximum_subarray(A,0,len(A)-1))
###############################################################################################################################