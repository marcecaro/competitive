# While partitioning arrays using Hoare Partition scheme, we make an 
#    assumption: The pivot element is always the first element of the array.

#                   _______ _____ _______
# The partion is   |<=pivot|pivot|>=pivot|
#                   ------- ----- -------

# arranca de las puntas acia el medio,  hasta que detecta una inversion
# algorithm partition(A, lo, hi) is
#     pivot := A[lo]
#     i := lo – 1
#     j := hi + 1
#     loop forever
#         do
#             i := i + 1
#         while A[i] < pivot

#         do
#             j := j – 1
#         while A[j] > pivot

#         if i >= j then
#             return j
#         swap A[i] with A[j]

def hoare(list):
    l=0
    h=len(list)-1
    pivot = list[0]
    while True:

        while list[l] < pivot: l+=1 ## Find an element that is >= to pivot
        while list[h] > pivot: h-=1 ## Find an element that is <= to pivot
        
        # After this point list[l] >= pivot and  list[h]<=pivot, they need to swap
        
        if l>=h:
            return h
        
        list[l], list[h] = list[h], list[l]
        l+=1
        h-=1


if __name__ == "__main__":
    lst= [4,3,5,4,4,6,1,2,7,4]
    pivot = hoare(lst)
    print(f"{lst}, has pivot array[{pivot}] == {lst[pivot]}")


