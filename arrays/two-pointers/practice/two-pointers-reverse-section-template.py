


def reverse(lst, b, e): # [b,e]
    pass

if __name__ == "__main__":

    original = [1,2,3, 4, 5, 6]
    lst = original[:]
    reverse(lst,0, 6)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [6,5,4,3,2,1]
    
    original = [1,2,3, 4, 5, 6]
    lst = original[:]
    reverse(lst,0, 3)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [3,2,1,4,5,6]

    original = [1,2,3, 4, 5, 6]
    lst = original[:]
    reverse(lst,4, 6)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [1,2,3, 4, 6, 5]

    original = [1,2,3, 4, 5, 6]
    lst = original[:]
    reverse(lst,0, 1)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [1,2,3, 4, 5, 6]