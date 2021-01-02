"""
[4, 2, 5, 6, 7, 3, 1]   = original list
[2, 4, 5, 6, 3, 1, 7]   = 7 is the largest in the list [4, 2, 5, 6, 7, 3, 1] --> move 7 to the end, move everything from the right of 7 to 7's position, i.e. [3,1] over
[2, 4, 5, 3, 1, 6, 7]   = 6 is the largest in the list [2, 4, 5, 6, 3, 1] --> move 6 to the end, move everything from the right of 6 to 6's position, i.e. [3,1] over
[2, 4, 3, 1, 5, 6, 7]   = 5 is the largest in the list [2, 4, 5, 3, 1] --> move 5 to the end, move everything from the right of 5 to 5's position, i.e. [3,1] over
[2, 3, 1, 4, 5, 6, 7]   = 4 is the largest in the list [2, 4, 3, 1] --> move 4 to the end, move everything from the right of 4 to 4's position, i.e. [3,1] over
[2, 1, 3, 4, 5, 6, 7]   = 3 is the largest in the list [2, 3, 1] --> move 3 to the end, move everything from the right of 3 to 3's position, i.e. [1] over
[1, 2, 3, 4, 5, 6, 7]   = 2 is the largest in the list [2, 1] --> move 2 to the end, move everything from the right of 2 to 2's position, i.e. [1] over
"""


def bubble_sort(L):
    """ (list) -> NoneType

    Sort the items of L from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    # The index of the last unsorted item.
    end = len(L) - 1

    while end != 0:

        # Bubble once through the unsorted section to move the largest item
        # to index end.
        for i in range(end):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]

        end = end - 1

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
