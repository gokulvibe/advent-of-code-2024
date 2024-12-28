from copy import deepcopy


def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-11/input.txt')

    input_list = list(map(int, file_input.split(' ')))

    prev_dict = {}
    for element in input_list:
        prev_dict[element] = prev_dict.get(element, 0) + 1

    for i in range(75):
        # print(i)
        new_dict = {}
        for num in prev_dict.keys():
            if num == 0:
                new_dict[1] = new_dict.get(1, 0) + prev_dict[num]
            elif len(str(num))%2 == 0:
                mid = len(str(num))//2
                new_num1 = int(str(num)[0:mid])
                new_num2 = int(str(num)[mid:])

                new_dict[new_num1] = new_dict.get(new_num1, 0) + prev_dict[num]
                new_dict[new_num2] = new_dict.get(new_num2, 0) + prev_dict[num]
            else:
                new_num = num * 2024
                new_dict[new_num] = new_dict.get(new_num, 0) + prev_dict[num]

        prev_dict = new_dict

    total_freq = 0
    for num, freq in prev_dict.items():
        total_freq+=freq
        
    print(total_freq)


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
