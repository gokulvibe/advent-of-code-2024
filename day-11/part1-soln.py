def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-11/input.txt')

    input_list = list(map(int, file_input.split(' ')))

    for i in range(6):
        # print(i)
        new_list = []
        for num in input_list:
            if num == 0:
                new_list.append(1)
            elif len(str(num))%2 == 0:
                mid = len(str(num))//2
                new_num1 = str(num)[0:mid]
                new_num2 = str(num)[mid:]
                new_list.append(int(new_num1))
                new_list.append(int(new_num2))
            else:
                new_list.append(num * 2024)

        input_list = new_list
        
    print(len(new_list))


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
