from HW_6.task_3 import eight_queens, random_eight_queens

queens = [(1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2), (8, 8)]
result = eight_queens(queens)
print(result)

cool_positions = random_eight_queens()
for position in cool_positions:
    print(position)
