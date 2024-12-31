def read_file_input(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def is_coordinate_within_boundaries(x, y, matrix):
    if x<0 or y<0 or x>len(matrix)-1 or y>len(matrix[0])-1:
        return False
    
    else:
        return True
