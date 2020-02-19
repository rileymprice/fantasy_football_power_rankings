import numpy as np

team_count = 10

winning = [
    (1, 3),
    (2, 5),
    (9, 7),
    (3, 6),
    (3, 1),
    (9, 2),
    (9, 8),
    (10, 6),
    (1, 10),
    (1, 2),
    (2, 6),
    (9, 6),
    (7, 6),
]
team_array = np.zeros((team_count, team_count), dtype=int)
team_final = {}
for winning_team, losing_team in np.ndindex(team_array.shape):
    if (winning_team + 1, losing_team + 1) in winning:
        team_array[winning_team, losing_team] = 1
square_team_array = np.matmul(team_array, team_array)
team_index = 1
for row in team_array:
    for value in row:
        # print(value)
        if team_index in team_final.keys():
            team_final[team_index] += value
        else:
            team_final[team_index] = value
    team_index += 1
team_index = 1
for row in square_team_array:
    for value in row:
        if team_index in team_final.keys():
            team_final[team_index] += value
        else:
            team_final[team_index] = value
    team_index += 1
print(team_final)
# print(team_array)
print(square_team_array)
# print(team_final)

