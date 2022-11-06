

def sort(lst):
    pass

if __name__ == "__main__":

    original = [4, 5, 6, 1,2,3 ]
    lst = original[:]
    sort(lst)

    print(f"Original: {original}, reversed: {lst}")
    assert lst == [1,2,3,4,5,6]
