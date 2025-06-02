def bubble_sort(my_list):
    list_length = len(my_list)
    for i in range(list_length - 1):
        for j in range(list_length - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

numbers = [8, 7, 5, 2, 4, 0, 2]
sorted_list = bubble_sort(numbers)
print(sorted_list)
