#
# left_rotation(lst, n) 
# n = n % len(lst)
#    |   A   |  B   |    ==> |   B   |  A   |
#            |n| 
#
# Algorithm
#     | A |  B   |
# while len(A) != len(B):
#      if len(A) < len(B):  | A  |      B       | 
#                           | A  | B1 | B       |
          #                 | B1 | A  | B       |         
#      if  len(A) > len(B):  | A          | B | 
#                            | A     | A1 | B | 
#                            | A     | B  | A1|
#
# swapBlock(A,B) 
#

def block_swap_left(lst, n):
    pass

if __name__ == "__main__":
    n =3
    original = [1,2,3,4,5,6,7,8,9]
    lst = original[:]
    block_swap_left(lst, n)

    print(f"Original: {original}, rotated {n}: {lst}")
    assert lst == [4, 5, 6, 7, 8, 9, 1, 2, 3]
    
    n = 6
    original = [1,2,3,4,5,6,7,8,9]
    lst = original[:]
    block_swap_left(lst, n)

    print(f"Original: {original}, rotated {n}: {lst}")
    assert lst == [7,8,9, 1,2,3,4,5,6]

    n = 1
    original = [1,2,3,4,5,6,7,8,9]
    lst = original[:]
    block_swap_left(lst, n)

    print(f"Original: {original}, rotated {n}: {lst}")
    assert lst == [2,3,4,5,6,7,8,9,1]

    n = 8
    original = [1,2,3,4,5,6,7,8,9]
    lst = original[:]
    block_swap_left(lst, n)

    print(f"Original: {original}, rotated {n}: {lst}")
    assert lst == [9,1,2,3,4,5,6,7,8]

    n = 9
    original = [1,2,3,4,5,6,7,8,9]
    lst = original[:]
    block_swap_left(lst, n)

    print(f"Original: {original}, rotated {n}: {lst}")
    assert lst == [1,2,3,4,5,6,7,8,9]

    n=0
    original = [1,2,3,4,5,6,7,8,9]
    lst = original[:]
    block_swap_left(lst, n)

    print(f"Original: {original}, rotated {n}: {lst}")
    assert lst == [1,2,3,4,5,6,7,8,9]










    