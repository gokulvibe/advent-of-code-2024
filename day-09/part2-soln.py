from copy import deepcopy

""" Solution is giving incorrect result """

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


def process_free_space(space_required, element, end_index, spaces_list, new_arr):
    for i, space in enumerate(spaces_list):
        if space[0] >= space_required:
            x = space[1]
            y = space[2]
            
            new_arr[x:x+space_required] = [element] * space_required
            new_arr[end_index-space_required+1:end_index+1] = ['.'] * space_required

            if space_required == space[0]:
                spaces_list.pop(i)
            else:
                space = (space[0]-space_required, x+space_required, y)
                spaces_list[i] = space

            break


def rearrange(arr):
    spaces_list = []

    start = 0
    end = 0
    for i, element in enumerate(arr):
        if element == '.':
            if start == end:
                start = i
                end = i
            end+=1
        
        elif element != '.' and start!=end:
            space = end-start

            space_entry = (space, start, end)
            spaces_list.append(space_entry)
            start = i
            end = i

        
    start = len(arr)-1
    end = len(arr)-1
    prev_element = arr[start]

    new_arr = deepcopy(arr)
    for i in range(len(arr)-1, -1, -1):
        element = arr[i]
        if element != prev_element and start != end:
            space = start - end
            if prev_element != '.':
                process_free_space(space, arr[start], start, spaces_list, new_arr)

            prev_element = element
            start = i
            end = i-1

        else:
            if start == end:
                start = i
                end = i
                prev_element = element
            end-=1

    
    return new_arr


def calculate_checksum(arr):
    checksum = 0
    for i, num in enumerate(arr):
        if num == '.':
            continue
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
