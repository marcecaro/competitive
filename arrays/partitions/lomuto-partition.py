# assumption: The pivot element is the last one
#       
# The partion is   |<pivot|pivot|>=pivot|
#       
# Two pointers are also maintained for tracking and comparison purposes:
#  i is scanning through the array, from its starting all the way to the end  
#  j is maintained to mark elements >= to the pivot
# Invariant:
#    [0,i] < pivot
#    (i,j] >= pivot
# Starting Point:
#     |                 | pivot |   
#     |j|->                       
#  |i|                          
# 
#
# Invariant:
# |  < pivot |   >=pivot     |... Not processed  ...|
# |                        |j|->
# |        |i|          
#



def lomuto(lst):

    if len(lst) <=1: return 0
    i=-1
    pivot_i=len(lst)-1
    pivot=lst[pivot_i]

    for j in range(0, len(lst)-1):
        if lst[j] >= pivot: 
            pass
        else:
            i+=1
            lst[j],lst[i] = lst[i], lst[j]
                
    i+=1
    lst[pivot_i],lst[i] = lst[i], lst[pivot_i]
    return i



if __name__ == "__main__":
    lst= [4,1,5,3,5,6,1,2,4,7,3,2]
    pivot = lomuto(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 1, 2, 3, 5, 6, 4, 2, 4, 7, 3, 5]
    
    lst= [4,1,5,3,5,6,1,2,7,3,2]
    pivot = lomuto(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 1, 2, 3, 5, 6, 4, 2, 7, 3, 5]

    lst= [4,1]
    pivot = lomuto(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 4]

    lst= [4,5,6,8]
    pivot = lomuto(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4,5,6,8]
    
    lst= [4,5]
    pivot = lomuto(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4,5]

    lst= [4,3]
    pivot = lomuto(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [3,4]










    