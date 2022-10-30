# assumption: The pivot element is the last one
#       
# The partion is   |<pivot|pivot|>=pivot|
#       
# Two pointers are also maintained for tracking and comparison purposes:
#  i is maintained to mark elements >= to the pivot 
#  j is scanning through the array, from its starting all the way to the end  
#
# Starting Point:
#  |                 | pivot |   
#  |i|               
#  |j|->
# 
#
# Invariant:
# |  < pivot |   >=pivot  | Not processed | pivot |
# |          |i|        |j|
#



def mcaro(lst):

    if len(lst) <=1: return 0
    i=0
    pivot_i = j
    pivot=lst[pivot_i]

    for j in range(0, len(lst)):
        if lst[i] >= pivot:
            