from constants import ANTINODE_SYMBOL

def check_coordinate_within_boundaries(x, y, matrix):
    if x<0 or y<0 or x>len(matrix)-1 or y>len(matrix[0])-1:
        return False
    else:
        return True


def calculate(matrix, soln_matrix):

    # Building the node coordinate mappings
    nodes = dict()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            node = matrix[i][j]
            if node != '.':
                if node in nodes:
                    nodes[node].append((i,j))
                else:
                    nodes[node] = [(i,j)]

    
    antinode_count = 0
    for node_key in nodes.keys():
        node = nodes[node_key]
        for i in range(len(node)-1):
            for j in range(i+1, len(node)):
                coordinate1 = node[i]
                coordinate2 = node[j]
                x1, y1 = coordinate1
                x2, y2 = coordinate2

                dx, dy = x1-x2, y1-y2

                # x3, x4 are the new coordinates for antinodes

                longest_dist = max(len(matrix), len(matrix[0]))
                for m in range(0, longest_dist+1):
                    x3 = x1 + m * dx
                    y3 = y1 + m * dy

                    if check_coordinate_within_boundaries(x3,y3, matrix):
                        matrix[x3][y3] = ANTINODE_SYMBOL
                    else:
                        break

                for m in range(0, longest_dist+1):
                    x4 = x2 - m * dx
                    y4 = y2 - m * dy

                    if check_coordinate_within_boundaries(x4,y4, matrix):
                        matrix[x4][y4] = ANTINODE_SYMBOL
                    else:
                        break

           

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ANTINODE_SYMBOL:
                antinode_count+=1

            # Created for debugging purpose
            # if soln_matrix[i][j] == ANTINODE_SYMBOL and matrix[i][j] != ANTINODE_SYMBOL:
            #     print((i, j))


    print(antinode_count)


def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-08/input.txt')

    matrix = file_input.split('\n')
    matrix = [list(row) for row in matrix]

    # Created for debugging purpose
    soln_matrix = read_file_input('day-08/soln.txt')

    soln_matrix = soln_matrix.split('\n')
    soln_matrix = [list(row) for row in soln_matrix]

    calculate(matrix, soln_matrix)

    pass

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
