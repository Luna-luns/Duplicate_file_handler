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


def print_error(error: Exception) -> None:
    print(error)


def print_duplicates(dupl: dict) -> None:
    for key, value in dupl.items():
        if len(value) > 1:
            print(f'\n{key} bytes')
            [print(value[i]) for i in range(len(value))]
        else:
            exit()
