# import numpy as np
''''''
#
# def render():
#     side_length = 15
#     display_width, display_height = 25, 50
#     cube_width, cube_height = side_length, int(side_length*(1/3))+side_length  # Assumes width is an additional 1/3 of height. To achieve this look use Courier new font on Windows terminal with 12ft size and 0.5 line spacing.
#     x, y, z = 1.0, 0.5 ,0.0
#
#     display_array = np.zeros((display_width, display_height), dtype=int)
#     corner_array_x = np.array([2,2,4,4,1,1,4,4], dtype=int)
#     corner_array_y = np.array([3,5,3,5,4,6,4,6], dtype=int)
#
#     def get_rx(theta):
#         return np.array([
#             [1, 0, 0],
#             [0, np.cos(theta), -np.sin(theta)],
#             [0, np.sin(theta), np.cos(theta)]
#         ])
#     def get_ry(theta):
#         return np.array([
#             [np.cos(theta), 0, np.sin(theta)],
#             [0, 1, 0],
#             [-np.sin(theta), 0, np.cos(theta)]
#         ])
#     def get_rz(theta):
#         return np.array([
#             [np.cos(theta), -np.sin(theta), 0],
#             [np.sin(theta), np.cos(theta), 0],
#             [0, 0, 1]
#         ])
#
#     def print_console():
#         for i in range(display_array.shape[0]):
#             for j in range(display_array.shape[1]):
#                 match display_array[i,j]:
#                     case 0:
#                         print("#", end='')
#                     case 1:
#                         print(".", end='')
#                     case 2:
#                         print("~", end='')
#                     case 3:
#                         print("%", end='')
#                     case 4:
#                         print("|", end='')
#                     case 5:
#                         print("=", end='')
#                     case _:
#                         print('x', end='')
#             print('\n')
#     print("\n")
#     print_console()
#     print()