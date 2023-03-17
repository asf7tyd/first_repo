def count_unique(lst):
    unique = set(lst)
    return len(unique)


my_list = [1, 2, 2, 3, 4, 4, 4, 5]
print(count_unique(my_list))
