def read_file_input(file_path):
    with open(file_path) as f:
        content = f.read()
    return content
