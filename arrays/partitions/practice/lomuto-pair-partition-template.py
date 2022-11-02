#       
# The partion is   |<even|odd|
#       
# Two pointers are also maintained for tracking and comparison purposes:
#  i is scanning through the array, from its starting all the way to the end  
#  j is maintained to mark elements >= to the pivot
# Invariant:
#    [0,i] are even
#    (i,j] are odd
# Starting Point:
#     |                   |   
#     |j|->                       
#  |i|                          
# 
#
# Invariant:
# |  < even |  odd |... Not processed  ...|
# |                |j|->
# |       |i|          
#


def is_even(n): return n%2==0

def lomuto_pair(lst):
   return 0


if __name__ == "__main__":
    lst= [4,1,5,3,5,6,1,2,4,7,3,2]
    pivot = lomuto_pair(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4, 6, 2, 4, 2, 1, 1, 5, 3, 7, 3, 5]
    
    lst= [4,1,5,3,5,6,1,2,7,3,2]
    pivot = lomuto_pair(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4, 6, 2, 2, 5, 1, 1, 5, 7, 3, 3]

    lst= [4,1]
    pivot = lomuto_pair(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4, 1]

    lst= [4,5,6,8]
    pivot = lomuto_pair(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4, 6, 8, 5]
    
    lst= [4,5]
    pivot = lomuto_pair(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4, 5]

    lst= [4,3]
    pivot = lomuto_pair(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4, 3]










    