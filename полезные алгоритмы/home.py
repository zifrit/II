l = [-1, 20, -10, 56, 5, -9, 8, 7, 6]

new_list = []
new_list1 = []

for i in range(len(l)):
    a = l[i]
    if a < 0:
        new_list.append(l[i])
    elif a > 0:
        new_list1.append(l[i])


print(new_list)
print(new_list1)

print('Минимальный элемент массива', min(l), 'его порядковый номер раен', l.index(max(l)))

# old_list = [1, 20, 10, 56, 5, 9, 8, 7, 6]
# # решил 2 способами. закомментированный первый способ
# # for i in range(len(l)):
# #     for j in range(len(l) - i - 1):
# #         if l[j] > l[j + 1]:
# #             l[j], l[j + 1] = l[j + 1], l[j]
# # print('Максимлаьный элемент массива', l[len(l) - 1], 'его порядковый номер раен', len(l) - 1)
# # нижже второй
# print('Максимлаьный элемент массива', max(l), 'его порядковый номер раен', l.index(max(l)))
#
#
# sorted(l)
#
# new_list = []
#
# while True:
#     for i in range(len(old_list)):
#         a = old_list[i]
#         if a % 2 != 0:
#             new_list.append(old_list[i])
#     if new_list == []:  # или elif not new_list
#         print('таких чисел нет')
#         break
#     elif new_list != []:  # или elif new_list
#         print('таких чисел етсь')
#         print(new_list)
#         break


