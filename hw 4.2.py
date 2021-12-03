my_list = [15, 89, 1, 6, 3, 55, 4, 4, 99, 10, 40, 12, 13]
new_list = [my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el-1]]
print(new_list)