def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst


my_list = [1, 2, 3, 4, 5]
print(change(my_list))
