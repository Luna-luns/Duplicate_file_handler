class DirectoryError(Exception):
    def __str__(self):
        return 'Directory is not specified'
