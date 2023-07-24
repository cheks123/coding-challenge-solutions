import re

def is_valid_phone(phone):
    pattern = r'^(070|080|090|081|091)([0-9]{8})$'
    result = re.fullmatch(pattern, phone)
    if result:
        return True
    return False
    

if __name__ == '__main__':
    print(is_valid_phone('07038147799'))
    print(is_valid_phone('0703814779'))
