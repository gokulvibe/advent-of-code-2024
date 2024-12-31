

def calculate_individual_perimeter(i, j, matrix):

    curr_plot = matrix[i][j]

    adjacent_plot_count = 0

    coordinates_inc =[
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    for dx, dy in coordinates_inc:
        adj_x = i+dx
        adj_y = j+dy


        if not is_coordinate_within_boundaries(adj_x, adj_y, matrix):
            continue

        adjacent_plot = matrix[adj_x][adj_y]
        if adjacent_plot == curr_plot:
            adjacent_plot_count+=1
        
    individual_perimeter = 4-adjacent_plot_count

    return individual_perimeter


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

            garden_area = len(garden_coordinates)
            garden_perimeter = 0
            for x, y in garden_coordinates:
                current_plot_permeter = calculate_individual_perimeter(x, y, matrix)
                garden_perimeter+=current_plot_permeter

            price = garden_area*garden_perimeter
            total_cost+=price

    print(total_cost)



if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from utils.common_utils import is_coordinate_within_boundaries
    main()
