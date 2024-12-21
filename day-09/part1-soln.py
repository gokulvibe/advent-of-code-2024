def expand_array(input_str):
    arr = []

    next_num = 0
    for i, count in enumerate(input_str):
        if i%2==0:
            arr += [next_num] * int(count)
            next_num+=1
        else:
            arr += ['.'] * int(count)

    return arr


def rearrange(arr):
    i = 0
    j = len(arr)-1

    while i<j:
        if arr[i] != '.':
            i+=1
            continue

        if arr[j] != '.':
            arr[i] = arr[j]
            arr[j] = '.'
            i+=1
            j-=1
            continue
        if arr[j] == '.':
            j-=1
            continue
    
    return arr


def calculate_checksum(arr):
    checksum = 0
    for i, num in enumerate(arr):
        if num == '.':
            break
        checksum+=num*i
    
    return checksum

def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-09/input.txt')


    arr = expand_array(file_input)
    arr = rearrange(arr)

    checksum = calculate_checksum(arr)

    print(checksum)


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
