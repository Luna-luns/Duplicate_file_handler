import os
import sys
from directory_error import DirectoryError


def get_directory():
    try:
        return sys.argv[1]
    except Exception:
        raise DirectoryError


try:
    args = get_directory()

    for root, dirs, files in os.walk(args, topdown=True):
        for name in files:
            print(os.path.join(root, name))

except DirectoryError as error:
    print(error)
