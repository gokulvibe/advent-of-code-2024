

def get_input_expressions():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-07/input.txt')
    input_expressions = []

    input_array = file_input.split('\n')
    for input in input_array:
        result, expression = input.split(':')

        result = int(result)
        expression = (result, list(map(int, expression.strip().split(" "))))
        input_expressions.append(expression)

    return input_expressions


def find_if_result(result, input_nums, curr_index, curr_result):
    if curr_result == result and curr_index == len(input_nums):
        return True
    if curr_index>=len(input_nums):
        return False

    return find_if_result(result, input_nums, curr_index+1, curr_result + input_nums[curr_index]) or find_if_result(result, input_nums, curr_index+1, curr_result * input_nums[curr_index])
    

def main():
    expressions = get_input_expressions()

    final_result = 0
    for expression in expressions:
        result = expression[0]
        input_nums = expression[1]

        if find_if_result(result=result, input_nums=input_nums, curr_index=1, curr_result=input_nums[0]):
            final_result+=result

    print("Sum of correct result possible expression's results: ", final_result)


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
