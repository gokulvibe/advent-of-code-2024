def main():
    from utils.common_utils import read_file_input
    file_input = read_file_input('day-07/input.txt')

if __name__ == '__main__':
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    main()
