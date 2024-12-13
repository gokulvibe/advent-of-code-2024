def read_file_input(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def find_xmas(matrix, x, y):
    if x==0 or y==0 or x==len(matrix)-1 or y==len(matrix[x])-1:
        return False

    if (
            (matrix[x+1][y+1] == 'M' and matrix[x-1][y-1] == 'S') or (matrix[x+1][y+1] == 'S' and matrix[x-1][y-1] == 'M')
        ) and (
            (matrix[x+1][y-1] == 'M' and matrix[x-1][y+1] == 'S') or (matrix[x+1][y-1] == 'S' and matrix[x-1][y+1] == 'M')
        ):
        return True
        


if __name__ == '__main__':
    try:
        input = read_file_input('day-04/input.txt')
        matrix = [list(row) for row in input.split('\n')]

        dx = [-1, 1, 0, 0, -1, -1, 1, 1]  # Change in rows (x-coordinates)
        dy = [0, 0, -1, 1, -1, 1, -1, 1]  # Change in columns (y-coordinates)

        sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 'A' and find_xmas(matrix, i, j):
                    sum+=1

        print(sum)
    except Exception as e:
        print(f'Error - {str(e)}')
        print(f'{i=}{j=}')