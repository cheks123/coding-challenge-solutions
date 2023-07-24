import re

def is_color_code(color):
    pattern = r'^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$'
    print('Valid') if re.fullmatch(pattern, color) else print('Invalid')
    return


if __name__ == '__main__':
    is_color_code('#abc123')
