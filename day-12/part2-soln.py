def is_a_corner(x, y, x1, y1, x2, y2, x3, y3, matrix):
    outer_corner_condition_side_1 = outer_corner_condition_side_2 = inner_corner = False
    current_plot = matrix[x][y]
    if not is_coordinate_within_boundaries(x1, y1, matrix):
        outer_corner_condition_side_1 = True
    
    if not is_coordinate_within_boundaries(x2, y2, matrix):
        outer_corner_condition_side_2 = True

    if not outer_corner_condition_side_1 and matrix[x1][y1] != current_plot:
            outer_corner_condition_side_1 = True

    if not outer_corner_condition_side_2 and matrix[x2][y2] != current_plot:
            outer_corner_condition_side_2 = True

    if is_coordinate_within_boundaries(x3, y3, matrix):
        inner_diagonal_plot = matrix[x3][y3]
        if inner_diagonal_plot != current_plot and matrix[x1][y1] == current_plot and matrix[x2][y2] == current_plot:
            inner_corner = True

    return (outer_corner_condition_side_1 and outer_corner_condition_side_2) or inner_corner


def find_number_of_corners(x, y, matrix):

    corners_count = 0

    coordinates_inc =[
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1,0)
    ]

    for i in range(len(coordinates_inc)-1):
        x1 = x+coordinates_inc[i][0]
        y1 = y+coordinates_inc[i][1]

        x2 = x+coordinates_inc[i+1][0]
        y2 = y+coordinates_inc[i+1][1]

        if i%2 == 0:
            x3 = x1
            y3 = y2
        else:
            x3 = x2
            y3 = y1


        if is_a_corner(x, y, x1, y1, x2, y2, x3, y3, matrix):
            corners_count+=1

    return corners_count


def get_a_garden(i, j, matrix, plot, visited):
    coordinates = []

    if not is_coordinate_within_boundaries(i, j, matrix):
        return coordinates

    if visited[i][j]:
        return coordinates

    if matrix[i][j] != plot:
        return coordinates

    coordinates.append((i,j))
    visited[i][j] = True

    coordinates_inc =[
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    for dx, dy in coordinates_inc:
        adj_x = i+dx
        adj_y = j+dy

        coordinates += get_a_garden(adj_x, adj_y, matrix, plot, visited)
    
    return coordinates


def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-12/input.txt')
    matrix = file_input.split('\n')
    matrix = [list(row) for row in matrix]

    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    total_cost = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
        
            plot = matrix[i][j]

            garden_coordinates = get_a_garden(i, j, matrix, plot, visited)

            if not garden_coordinates:
                continue

            garden_area = len(garden_coordinates)
            total_corners = 0       # number of corners = num of edges (new perimeter in part 2)
            for x, y in garden_coordinates:
                number_of_corners = find_number_of_corners(x, y, matrix)
                total_corners+=number_of_corners

            price = garden_area*total_corners
            total_cost+=price

    print(total_cost)


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from utils.common_utils import is_coordinate_within_boundaries
    main()
