from typing import Annotated, Tuple

recursion_count = 0

def coordinate_inc_for_direction(direction) -> Tuple[Annotated[int, 'x_inc'], Annotated[int, 'y_inc']]:
    inc_x_y = {
            'up': (-1, 0),
            'down': (1, 0),
            'left': (0, -1),
            'right': (0, 1)
        }
    return inc_x_y[direction]


def get_input_matrix():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-06/input.txt')
    matrix = [list(row) for row in file_input.split('\n')]

    return matrix


def evaluate_exit_condition(x, y, direction, matrix):
    if (x == 0 and direction == 'up') \
        or (y == 0 and direction == 'left') \
            or (x == len(matrix)-1 and direction == 'down') \
                or (y == len(matrix[0])-1 and direction == 'right'):
        return True
    else:
        return False
    


def get_alternate_direction(direction):
    alternate_direction = {
        'up': 'right',
        'right': 'down',
        'down': 'left',
        'left': 'up'
    }

    return alternate_direction[direction]



def get_next_direction(x, y, direction, matrix):
    next_direction = direction

    x_inc, y_inc = coordinate_inc_for_direction(direction)

    next_value = matrix[x+x_inc][y+y_inc]
    if next_value == '#':
        next_direction = get_alternate_direction(direction)

    return next_direction


def mark_with_dfs(x, y, direction, matrix):
    if evaluate_exit_condition(x, y, direction, matrix):
        matrix[x][y] = 'X'
        return matrix

    matrix[x][y] = 'X'

    direction = get_next_direction(x, y, direction, matrix)

    x_inc, y_inc = coordinate_inc_for_direction(direction)

    global recursion_count
    
    recursion_count+=1
    matrix = mark_with_dfs(x+x_inc, y+y_inc, direction, matrix)

    return matrix


def find_start_position(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == '^':
                return x, y
    
    return 0,0  # Default condition which probably won't occur


def calculate_visited_count(matrix):
    visited_count = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == 'X':
                visited_count+=1

    return visited_count

def main():
    try:
        """
        Recursion solution - reaches maximum depth for the given input
        """
        matrix = get_input_matrix()
        x, y = find_start_position(matrix)
        matrix = mark_with_dfs(x, y, 'up', matrix)

        visited_count = calculate_visited_count(matrix)

        print(visited_count)

    except RecursionError as r:
        print(str(r))
        print(f"{recursion_count=}")


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
