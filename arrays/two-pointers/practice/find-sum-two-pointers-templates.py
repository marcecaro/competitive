
def find_sum(lst, n):
    return (0, 0)

if __name__ == "__main__":

    n = 14
    original = [1,2,3,6,5,4,2,10,99]
    lst = original[:]
    found = find_sum(lst, n)

    print(f"Original: {original}, found {n}: {found}")
    assert found == (4,10)

    n = 5
    original = [1,2,3,6,5,4,2,10,99]
    lst = original[:]
    found = find_sum(lst, n)

    print(f"Original: {original}, found {n}: {found}")
    assert found == (1,4)

    n = 4
    original = [1,2,3,6,5,4,2,10,99]
    lst = original[:]
    found = find_sum(lst, n)

    print(f"Original: {original}, found {n}: {found}")
    assert found == (1,3)

    n = 109
    original = [1,2,3,6,5,4,2,10,99]
    lst = original[:]
    found = find_sum(lst, n)

    print(f"Original: {original}, found {n}: {found}")
    assert found == (10,99)

    n = 110
    original = [1,2,3,6,5,4,2,10,99]
    lst = original[:]
    found = find_sum(lst, n)

    print(f"Original: {original}, found {n}: {found}")
    assert found == (0,0)