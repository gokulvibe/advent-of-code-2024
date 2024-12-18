from copy import deepcopy
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


def encode_obstacle_visit(x, y, direction):
    return f"{x}_{y}_{direction}"


def get_next_direction(x, y, direction, matrix, obstacle_visits):
    next_direction = direction

    x_inc, y_inc = coordinate_inc_for_direction(direction)

    next_value = matrix[x+x_inc][y+y_inc]
    if next_value == '#' or next_value=='O':    # O indicates user added new obstacle
        obstacle_visits.add(encode_obstacle_visit(x,y,direction))
        next_direction = get_alternate_direction(direction)

    return next_direction


def is_there_a_loop(x, y, direction, matrix, obstacle_x, obstacle_y):
    matrix = matrix.copy()
    obstacle_visits = set()
    if x==6 and y==3:
        pass

    iter=0
    while not evaluate_exit_condition(x, y, direction, matrix):
        if encode_obstacle_visit(x,y,direction) in obstacle_visits:
            print(f"returning True, {obstacle_x=} {obstacle_y=} {iter=}")
            return True

        matrix[x][y] = 'X'

        direction = get_next_direction(x, y, direction, matrix, obstacle_visits)

        x_inc, y_inc = coordinate_inc_for_direction(direction)

        x=x+x_inc
        y=y+y_inc

        iter+=1

    print(f"While loop done - {obstacle_x=} {obstacle_y=} {iter=}")

    matrix[x][y] = 'X'
    return False



def mark_the_route(x, y, direction, matrix):
    
    while not evaluate_exit_condition(x, y, direction, matrix):
        matrix[x][y] = 'X'

        direction = get_next_direction(x, y, direction, matrix, set())

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
    Recursion solution - reaches maximum depth for the given input
    """
    matrix = get_input_matrix()
    x, y = find_start_position(matrix)

    route_marked_matrix = mark_the_route(x, y, 'up', matrix)

    loop_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            arg_matrix = deepcopy(route_marked_matrix)
            if i==6 and j==3:
                pass
            if (i!=x and j!=y) and arg_matrix[i][j]=='X':
                arg_matrix[i][j] = 'O'
                
                is_loop = is_there_a_loop(x, y, 'up', arg_matrix, i, j)

                if is_loop:
                    loop_count+=1

    print("Num of blocks visited: ", loop_count)



if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
