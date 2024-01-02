import sys
from parser.validation import ImportValidator


def main():
    args = sys.argv
    ImportValidator(args).validate()


if __name__ == '__main__':
    main()
