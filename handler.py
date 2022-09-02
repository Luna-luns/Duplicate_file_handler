import os
import sys
from directory_error import DirectoryError
import ui


def get_directory():
    try:
        return sys.argv[1]
    except Exception:
        raise DirectoryError


s_dict = {}
try:
    args = get_directory()
    file_format = ui.get_format()

    for root, dirs, files in os.walk(args):
        for name in files:
            path = os.path.join(root, name)

            if file_format:
                split_path = os.path.splitext(path)

                if split_path[1] == '.' + file_format:
                    path = split_path[0] + split_path[1]
                else:
                    continue

            size = os.path.getsize(path)
            if s_dict.get(size) is None:
                s_dict[size] = [path]
            else:
                s_dict[size].append(path)

except DirectoryError as error:
    ui.print_error(error)

ui.print_options()
option = ui.get_option()

if option == '1':
    ui.print_duplicates(s_dict)
else:
    ui.print_duplicates({key: value for key, value in sorted(s_dict.items(), key=lambda item: item[0])})
