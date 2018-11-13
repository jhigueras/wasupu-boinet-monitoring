import sys

from boinet_monitoring import cli


def main():
    if len(sys.argv) > 1:
        args = cli.build_parser().parse_args()
        args.func(args)
    else:
        print("Missing arguments. Use the the help argument (-h) to get the list of arguments")


main()
