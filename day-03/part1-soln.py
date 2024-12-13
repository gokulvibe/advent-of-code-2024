import re


def read_file_input(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def get_regex_matches(pattern, input):
    matches = re.findall(pattern, input)
    return matches

def get_multiplicants(match):
    nums = tuple(map(int, get_regex_matches(pattern=r'\d+', input=match)))
    return nums[0], nums[1]

def get_valid_multiplication_expressions(input):
    matches = get_regex_matches(pattern=r"mul\(\d+,\d+\)", input=input)
    return matches

def find_total_sum(matches):
    total_sum = 0
    for match in matches:
        num1, num2 = get_multiplicants(match=match)
        total_sum+= num1*num2
    
    return total_sum


if __name__ == '__main__':
    input = read_file_input(file_path='day-03/input.txt')

    matches = get_valid_multiplication_expressions(input=input)

    total_sum = find_total_sum(matches=matches)

    print(total_sum)
