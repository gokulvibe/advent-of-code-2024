from typing import Dict, List


def construct_rules_dict(rules: List) -> Dict:
    rules_dict = {}
    for rule in rules:
        higher, lower = rule.split('|')
        if higher in rules_dict:
            rules_dict[higher].add(lower)
        else:
            rules_dict[higher] = {lower}
    return rules_dict


def get_invalid_pages(page_updates: Dict, rules_dict: Dict) -> List:
    invalid_pages = []
    for update in page_updates:
        update = update.split(',')
        for i, entry in enumerate(update):
            if entry not in rules_dict:
                break
            later_elements = set(update[i+1:])
            allowed_later_elements = rules_dict[entry]

            intersection = later_elements.intersection(allowed_later_elements)
            if len(intersection) != len(later_elements):
                invalid_pages.append(update)
                break

    return invalid_pages


def make_pages_valid(invalid_pages: List, rules_dict: Dict) -> List:
    from functools import cmp_to_key
    def custom_valid_entry_comparator(a, b):
        if a in rules_dict.get(b, []):
            return 1  # `a` is in b's rule book, so it should come after `b` in a valid page
        if b in rules_dict.get(a, []):
            return -1  # `b` is in a's rule book, so it should come after `a` in a valid page
        return 0  # They are equal in terms of sorting

    valid_pages = []
    for page in invalid_pages:
        valid_page = sorted(page, key=cmp_to_key(custom_valid_entry_comparator))
        valid_pages.append(valid_page)

    return valid_pages


def get_mid_sum(valid_pages: List) -> int:
    mid_sum = 0
    for valid_page in valid_pages:
        mid = len(valid_page)//2
        mid_sum+=int(valid_page[mid])

    return mid_sum


def main():
    from utils.common_utils import read_file_input

    file_input = read_file_input('day-05/input.txt')

    input_parts = file_input.split('\n\n')

    rules = input_parts[0]
    page_updates = input_parts[1]

    rules = rules.split('\n')
    page_updates = page_updates.split('\n')

    rules_dict = construct_rules_dict(rules=rules)

    invalid_pages = get_invalid_pages(page_updates, rules_dict)

    valid_pages = make_pages_valid(invalid_pages, rules_dict)
   
    mid_sum = get_mid_sum(valid_pages=valid_pages)

    print(mid_sum)


if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
