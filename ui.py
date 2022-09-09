from option_error import OptionError


def get_format() -> str:
    return input('Enter file format: ' + '\n').strip()


def print_options() -> None:
    print('\nSize sorting options:\n1. Descending\n2. Ascending')


def get_option() -> str:
    while True:
        try:
            option = input('\n' + 'Enter a sorting option: ' + '\n').strip()
            if option not in ('1', '2'):
                raise OptionError
            return option
        except OptionError as error:
            print()
            print_error(error)


def get_permission() -> str:
    while True:
        try:
            option = input('\n' + 'Check for duplicates?' + '\n').strip()
            if option not in ('yes', 'no'):
                raise OptionError
            return option
        except OptionError as error:
            print(error)


def print_error(error: Exception) -> None:
    print(error)


def print_duplicates(dupl: dict) -> None:
    for key, value in dupl.items():
        if len(value) > 1:
            print(f'\n{key} bytes')
            [print(value[i]) for i in range(len(value))]
        else:
            continue


def print_hashes(h_dict: dict) -> None:
    count = 0
    for key, value in h_dict.items():
        print(f'\n{key} bytes')
        for k, v in value.items():
            if len(v) > 1:
                print(f'Hash: {k}')
                for i in range(len(v)):
                    print(f'{count + 1}. {v[i]}')
                    count += 1
        else:
            continue
