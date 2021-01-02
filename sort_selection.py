"""
[4, 2, 5, 6, 7, 3, 1]   = original list
[1, 2, 5, 6, 7, 3, 4]   = 1 is the smallest in list [4, 2, 5, 6, 7, 3, 1] --> swap position with the first item 4 
[1, 2, 5, 6, 7, 3, 4]   = 2 in the smallest in list [2, 5, 6, 7, 3, 4] --> no need to swap
[1, 2, 3, 6, 7, 5, 4]   = 3 in the smallest in list [5, 6, 7, 3, 4] --> swap position with the first item 5
[1, 2, 3, 4, 7, 5, 6]   = 4 in the smallest in list [6, 7, 5, 4] --> swap position with the first item 6
[1, 2, 3, 4, 5, 7, 6]   = 5 in the smallest in list [7, 5, 6] --> swap position with the first item 7
[1, 2, 3, 4, 5, 6, 7]   = 6 in the smallest in list [7, 6] --> swap position with the first item 7
[1, 2, 3, 4, 5, 6, 7]
"""

def get_index_of_smallest(L, i):
    """ (list, int) -> int

    Return the index of the smallest item in L[i:].

    >>> get_index_of_smallest([2, 7, 3, 5], 1)
    2
    """

    # The index of the smallest item so far.
    index_of_smallest = i

    for j in range(i + 1, len(L)):
        if L[j] < L[index_of_smallest]:
            index_of_smallest = j

    return index_of_smallest

    
def selection_sort(L):
    """ (list) -> NoneType

    Sort the items of L from smallest to largest.

    >>> L = [3, 7, 2, 5]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    """

    
    for i in range(len(L)):

        # Find the index of the smallest item in L[i:] and swap that
        # item with the item at index i.

        index_of_smallest = get_index_of_smallest(L, i)
        L[index_of_smallest], L[i] = L[i], L[index_of_smallest]



if __name__ == '__main__':
    import doctest
    doctest.testmod()
