


def reverse(lst):
    b=0
    e=len(lst)-1
    while b<e:
        lst[b], lst[e] = lst[e], lst[b]
        b+=1
        e-=1

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