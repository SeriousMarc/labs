def get_bubble_sorted_list(lst):

    """
        Function sorts given list of numbers (int) by bubble sort algorithm.
        If non-integer and non-float element is given, the function will pass it.
        :param lst: list of numbers (int or float) to sort (list).
        :return: sorted list (list).
    """

    lst_to_sort = [elem for elem in lst if type(elem) == int]
    for num in range(len(lst_to_sort) - 1, 0, -1):
        for index in range(num):
            if lst_to_sort[index] > lst_to_sort[index + 1]:
                lst_to_sort[index], lst_to_sort[index + 1] = lst_to_sort[index + 1], lst_to_sort[index]

    return lst_to_sort
