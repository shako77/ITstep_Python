# 1.
# import random
#
# my_list = ["car", "bicycle", "motorcycle", "airplane", "truck"]
#
# random = random.choice(my_list)
#
# user_input = input("გამოიცანით სიტყვა: ")
#
# if user_input == random:
#     print("თქვენი არჩევანი სწორია")
#
# elif user_input != random:
#     print("თქვენი არჩევანი არასწორია")
#
# if user_input != random:
#     print("სწორი პასუხი იყო:", random)







# 2.
# my_list = [43, "22", 12, 66, 210, ["hi"]]
# print( my_list)
#
# index = my_list.index(210)
# print("210 ინდექსი არის", index)
#
# my_list.append("hello")
# print("ახალი ლისტი არის", my_list)
#
# my_list.remove(12)
# print("ახალი ლისტი არის", my_list)







# 3.

# def transpose(matrix):
#
#     transposed = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     for i in range(3):
#         for j in range(3):
#             transposed[j][i] = matrix[i][j]
#     return transposed
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# transposed_matrix = transpose(matrix)
#
# for row in transposed_matrix:
#     print(row)
