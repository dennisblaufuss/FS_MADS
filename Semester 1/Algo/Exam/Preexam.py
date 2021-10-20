# Dennis Blaufuss
# 18.10.21

mat = [[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]


def return_smallest(in_l):
    """returns the smallest common integer in set of lists

    Args:
        in_l (list): Has to be a list containing lists of the same lenght
    """
    i = 0
    while True:
        # since its a matrix and hence every row should have equal len,
        # we only have to check for the first lenght
        if i == len(in_l[0]):
            return - 1
        in_all_list = True
        for check_l in in_l:
            temp_bool = in_l[0][i] in check_l
            in_all_list &= temp_bool
            if not in_all_list:
                break
        if in_all_list:
            return in_l[0][i]
        i += 1


print(return_smallest(mat))

"""
The Function runs through the first list and checks item after item if this exact item is contained every other list as well.
The Function breaks at two possible points:
1 The Function has found and item i in the first list, that is contained in every other one as well. -> the function prints that exact item
2 The Function has run through all of the items of the first list and has not found any hit (thus no item is in all of the lists). -> the function prints -1
"""
