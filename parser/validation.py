from re import match


class ImportValidator:
    def __init__(self, args: list):
        self.__args = args

    def validate(self) -> None:
        if len(self.__args) != 3:
            raise Exception('Invalid arguments count')
        self.__validate_url(self.__args[1])

    def __validate_url(self, url: str) -> None:
        if not match('^https://debank.com/profile/0x[0-9a-fA-F]+$', url):
            raise Exception('Invalid URL format')

    def __validate_filename(self, filename: str) -> None:
        if not match('^(.+)\/([^\/]+)$', filename):
            raise Exception('Invalid filename format')
