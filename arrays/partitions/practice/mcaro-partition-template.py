#
# The partion is   |<pivot|pivot|>=pivot|
#       
# Two pointers are also maintained for tracking and comparison purposes:
#  i is maintained to mark elements >= to the pivot is scanning through the array, from its starting all the way to the end  
#  j 
#
# Starting Point:
#  |                 | pivot |   
#  |i|->               
#                  <-|   j   |
# 
#
# Invariant:
# [i,j): Not proccecced
# [0,i):   <  pivot
# [j:len): >= pivot
#
# |  < pivot |Not processed|>=pivot|pivot|
# |          |i|           |j|
#



def mcaro(lst):
    return 0

if __name__ == "__main__":
    lst= [4,1,5,3,5,6,1,2,4,7,3,2]
    pivot = mcaro(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 1, 2, 5, 6, 5, 2, 4, 7, 3, 4, 3]
    
    lst= [4,1,5,3,5,6,1,2,7,3,2]
    pivot = mcaro(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 1, 2, 5, 6, 5, 2, 7, 3, 4, 3]

    lst= [4,1]
    pivot = mcaro(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [1, 4]

    lst= [4,5,6,8]
    pivot = mcaro(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4,5,6,8]
    
    lst= [4,5]
    pivot = mcaro(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [4,5]

    lst= [4,3]
    pivot = mcaro(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")
    assert lst == [3,4]










    