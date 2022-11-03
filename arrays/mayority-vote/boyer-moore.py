


def mayority_bm(lst):
   n = len(lst)//2

   candidate = 0
   count = 0
   for i in lst:

    if count==0:
        candidate=i
        count = 1

    if i==candidate:
        count += 1
    else:
        count -=1


    count = 0
    for i in lst:
        if i == candidate:
            count+=1
    
    if count>n: return candidate
    else: return None


if __name__ == "__main__":

    original = [1,2,3,1,1]
    lst = original[:]
    n = mayority_bm(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == 1

    original = [1,2,3,4]
    lst = original[:]
    n = mayority_bm(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == None

   
    original = [1]
    lst = original[:]
    n = mayority_bm(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == 1

    original = [1,2,1,2]
    lst = original[:]
    n = mayority_bm(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == None

    original = []
    lst = original[:]
    n = mayority_bm(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == None