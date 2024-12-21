from constants import ANTINODE_SYMBOL

def check_coordinate_within_boundaries(x, y, matrix):
    if x<0 or y<0 or x>len(matrix)-1 or y>len(matrix[0])-1:
        return False
    else:
        return True


def calculate(matrix):

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
                x3 = x1 + dx
                y3 = y1 + dy

                x4 = x2 - dx
                y4 = y2 - dy

                if check_coordinate_within_boundaries(x3,y3, matrix):
                    matrix[x3][y3] = ANTINODE_SYMBOL
                if check_coordinate_within_boundaries(x4,y4, matrix):
                    matrix[x4][y4] = ANTINODE_SYMBOL
           

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == ANTINODE_SYMBOL:
                antinode_count+=1
    
    print(antinode_count)


def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-08/input.txt')

    matrix = file_input.split('\n')
    matrix = [list(row) for row in matrix]

    calculate(matrix)

    pass

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
