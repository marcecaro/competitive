


def mayority(lst):
   m = 0
   mc = 0
   for i in lst:
    c = 0
    for j in lst:
        if i==j:
            c+=1
            if c>mc:
                m=i
                mc=c
    if mc > len(lst)//2: return m
    else: return None


if __name__ == "__main__":

    original = [1,2,3,1,1]
    lst = original[:]
    n = mayority(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == 1

    original = [1,2,3,4]
    lst = original[:]
    n = mayority(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == None

   
    original = [1]
    lst = original[:]
    n = mayority(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == 1

    original = [1,2,1,2]
    lst = original[:]
    n = mayority(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == None

    original = []
    lst = original[:]
    n = mayority(lst)

    print(f"Original: {original}, mayority: {n}")
    assert n == None