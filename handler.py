import os
import sys
from directory_error import DirectoryError
import ui
import hashlib


def get_directory():
    try:
        return sys.argv[1]
    except Exception:
        raise DirectoryError


def get_count(ha_dict: dict) -> int:
    count = 0
    for key, value in ha_dict.items():
        for k, v in value.items():
            if len(v) > 1:
                count += len(v)
            else:
                continue
    return count


def delete_files(nums: list, ha_dict: dict) -> int:
    bytes_free = 0
    count = 0
    for key, value in ha_dict.items():
        for k, v in value.items():
            if len(v) > 1:
                for i in range(len(v)):
                    _file = f'{count + 1}. {v[i]}'.split('. ')
                    if int(_file[0]) in nums:
                        bytes_free += key
                        os.remove(_file[1])
                    count += 1
            else:
                continue
    return bytes_free


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
    ui.print_duplicates({key: value for key, value in sorted(s_dict.items(), key=lambda item: item[0], reverse=True)})
else:
    ui.print_duplicates({key: value for key, value in sorted(s_dict.items(), key=lambda item: item[0])})

permission = ui.get_permission()
hash_dict = {}
if permission == 'yes':

    for key, value in s_dict.items():
        for file in value:
            with open(file, 'rb') as f:
                f_hash = hashlib.md5(f.read(key)).hexdigest()

                if hash_dict.get(key) is None:
                    hash_dict[key] = {f_hash: [file]}
                else:
                    d = hash_dict[key]
                    if f_hash in d:
                        d[f_hash].append(file)
                    else:
                        d.update({f_hash: [file]})
    if option == '1':
        ui.print_hashes({key: value for key, value in sorted(hash_dict.items(), key=lambda item: item[0], reverse=True)})
    else:
        ui.print_hashes({key: value for key, value in sorted(hash_dict.items(), key=lambda item: item[0])})
else:
    exit()

del_answer = ui.get_delete_answer()

if del_answer == 'yes':
    if option == '1':
        h_dict = {key: value for key, value in sorted(hash_dict.items(), key=lambda item: item[0], reverse=True)}
        numbers = ui.get_file_numbers(get_count(h_dict))
        ui.print_freed_up_bytes(delete_files(numbers, h_dict))
    else:
        h_dict = {key: value for key, value in sorted(hash_dict.items(), key=lambda item: item[0])}
        numbers = ui.get_file_numbers(get_count(h_dict))
        ui.print_freed_up_bytes(delete_files(numbers, h_dict))
else:
    exit()
