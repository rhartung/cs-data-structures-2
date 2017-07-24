#Sorting


def bubble_sort(lst):
    """Returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap.

        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    for i in range(len(lst) - 1):

        swap = False
        # each loop through do not need to check already sorted part of list
        for j in range(len(lst) - 1 - i):

            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True

        # win fast solution - if prev run did not swap, break loop
        if not swap:
            break

    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list
    containing all integers in the input lists.

    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    merged_list = []

    while len(list1) > 0 or len(list2) > 0:

        # if list one or list 2 is empty then only need to pop from other
        # non-empty list
        if not list1:
            merged_list.append(list2.pop(0))

        elif not list2:
            merged_list.append(list1.pop(0))

        # compare index 0 of both sorted lists to get lower value
        # append lower value to new list until all values sorted
        elif list1[0] > list2[0]:
            merged_list.append(list2.pop(0))

        else:
            merged_list.append(list1.pop(0))

    return merged_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.

    Finish the merge sort algorithm by writing another function that takes in a
    single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all
    integers from the input list. In other words, the new function should sort
    a list using merge_lists and recursion.

    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    # list of 1 or fewer items is already sorted
    if len(lst) < 2:
        return lst

    center = len(lst) / 2

    # divide list down to many lists containing one item each to be compared
    # compare using merge_lists function until all values sorted
    one_half = merge_sort(lst[center:])
    other_half = merge_sort(lst[:center])

    return merge_lists(one_half, other_half)


#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
