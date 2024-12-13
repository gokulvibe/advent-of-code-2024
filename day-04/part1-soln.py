
def read_file_input(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def backtrack(matrix, x, y, x_inc, y_inc, curr, result_word):
    try:
        if x<0 or y<0 or x>=len(matrix) or y>=len(matrix[x]):
            return 0

        if matrix[x][y] != result_word[curr]:
            return 0

        if curr == len(result_word) - 1 and matrix[x][y] == result_word[curr]:
            return 1
        
        return backtrack(matrix, x+x_inc, y+y_inc, x_inc, y_inc, curr+1, result_word) \
           
    except Exception as e:
        print(f"Error in backtrack - {str(e)}")
        print(f"{x=} {y=} {curr=}")
        raise e



if __name__ == '__main__':
    try:
        input = read_file_input('day-04/input.txt')
        matrix = [list(row) for row in input.split('\n')]

        dx = [-1, 1, 0, 0, -1, -1, 1, 1]  # Change in rows (x-coordinates)
        dy = [0, 0, -1, 1, -1, 1, -1, 1]  # Change in columns (y-coordinates)

        sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                for c in range(8):
                    sum += backtrack(matrix=matrix, x=i, y=j, x_inc=dx[c], y_inc=dy[c], curr=0, result_word='XMAS')

        print(sum)
    except Exception as e:
        print(f'Error - {str(e)}')
        print(f'{i=}{j=}')
