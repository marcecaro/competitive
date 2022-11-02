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
    n = n % len(lst)
    if n == 0: return
    ab = 0
    ae = n
    bb = n
    be = len(lst)

    def sizeA(): return ae-ab
    def sizeB(): return be-bb

    while sizeA() != sizeB():
        if sizeA() < sizeB():
            swapSize = sizeA()
            b1b = bb
            b1e = bb + swapSize
            bb  = b1e
            lst[ab:ae], lst[b1b:b1e] = lst[b1b:b1e], lst[ab:ae]
            ab=b1b
            ae=b1e
        if sizeB() < sizeA():
            swapSize=sizeB()
            ae  = ae - swapSize
            a1b = ae
            a1e  = bb
            lst[bb:be], lst[a1b:a1e] = lst[a1b:a1e] , lst[bb:be]
            bb = a1b
            be = a1e
    lst[ab:ae], lst[bb:be] = lst[bb:be], lst[ab:ae]






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










    