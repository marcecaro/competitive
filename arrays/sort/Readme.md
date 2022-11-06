# Sorting algorithms

## Selection Sort
order      O(2)
stable     NO
in-place   YES

Start:      n=len(A) - 1
Invariant: 
    [0, n]  : un ordered
    (n, len): Orered
           

    1) Find the index of the largest number in [0, n] ~> l
    2) swap(A,l,n)
    3) n-=1
    4) Goto 1


## Insertion Sort
order      O(2)
stable     YES
in-place   YES

Start:      n=len(A) - 1
Invariant: 
    [n, len): Orered
    [0, n)  : un ordered

    1) j = n-1
    2) insert in the right possition in -> A[n, len]
    3) n-=1
    4) Goto 1

## Merge Sort
order      O(nlog(n))
stable     YES
in-place   NO

- Needs to allocate memeory
- Order the the two half of the array, then merge them


## Quick Sort
order      O(n2)/ average -> O(nlog(n))
stable     NO
in-place   YES

- Use partition and pivot



# TODO
[ ] Bucket Sort
[ ] Radix