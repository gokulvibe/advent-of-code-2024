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
    matches = get_regex_matches(pattern=r"(?!.*don't\(.*?)(mul\(\d+,\d+\))(?!.*?do\()", input=input)
    return matches

def find_total_sum(matches):
    total_sum = 0
    for match in matches:
        num1, num2 = get_multiplicants(match=match)
        total_sum+= num1*num2
    
    return total_sum


# By ChatGPT
def find_valid_mul(text):
    # Step 1: Find all ranges of `don't()` ... `do()`
    ignore_ranges = []
    for match in re.finditer(r"don't\(.*?do\(", text, re.DOTALL):
        ignore_ranges.append((match.start(), match.end()))

    # Step 2: Find all `mul(a,b)`
    mul_matches = []
    for match in re.finditer(r"mul\(\d+,\d+\)", text):
        start, end = match.start(), match.end()
        
        # Check if the match is outside the excluded ranges
        if not any(ignore_start <= start < ignore_end for ignore_start, ignore_end in ignore_ranges):
            mul_matches.append(match.group())
    
    return mul_matches
    

if __name__ == '__main__':
    input = read_file_input(file_path='day-03/input.txt')

    # My solution didn't work
    # matches = get_valid_multiplication_expressions(input=input)

    # ChatGPT solution
    matches = find_valid_mul(input)

    total_sum = find_total_sum(matches=matches)

    print(total_sum)
