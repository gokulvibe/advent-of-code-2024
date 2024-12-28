def calculate_correct_paths(i, j, prev_number, matrix, visited):
    if i<0 or j<0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] == '.' or (i, j) in visited:
        return 0

    visited.add((i,j))

    if int(matrix[i][j]) == 9 and prev_number == 8:
        return 1
    
    if prev_number is not None and int(matrix[i][j]) != prev_number+1:
        visited.remove((i,j))
        return 0


    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    correct_paths = 0
    for dx, dy in directions:
        path_score = calculate_correct_paths(i=i+dx, j=j+dy, prev_number=int(matrix[i][j]), matrix=matrix, visited=visited)
        correct_paths+=path_score

    visited.remove((i,j))
    return correct_paths


def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-10/input.txt')

    matrix = file_input.split('\n')
    matrix = [list(row) for row in matrix]

    total_score = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '0':
                visited = set()
                score = calculate_correct_paths(i, j, None, matrix, visited)

                total_score+=score

    print(total_score)



if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
