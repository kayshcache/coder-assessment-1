import os

def check_valid_file(path):
    if os.path.exists(path):
        return os.path.isfile(path) # line above is reduntant because this line does both checks
    return False

output = check_valid_file()
print(output)
