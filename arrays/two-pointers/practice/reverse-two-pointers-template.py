


def reverse(lst):
    pass

if __name__ == "__main__":

    original = [1,2,3]
    lst = original[:]
    reverse(lst)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [3,2,1]

    original = [1,2]
    lst = original[:]
    reverse(lst)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [2,1]

    original = [1]
    lst = original[:]
    reverse(lst)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [1]

    original = []
    lst = original[:]
    reverse(lst)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == []