from typing import Annotated, Tuple

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


def mark_with_looping(x, y, direction, matrix):
    
    while not evaluate_exit_condition(x, y, direction, matrix):
        matrix[x][y] = 'X'

        direction = get_next_direction(x, y, direction, matrix)

        x_inc, y_inc = coordinate_inc_for_direction(direction)

        x=x+x_inc
        y=y+y_inc

    matrix[x][y] = 'X'
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
    """
    Non recursive soln
    """
    matrix = get_input_matrix()
    x, y = find_start_position(matrix)
    matrix = mark_with_looping(x, y, 'up', matrix)

    visited_count = calculate_visited_count(matrix)

    print("Num of blocks visited: ", visited_count)



if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
