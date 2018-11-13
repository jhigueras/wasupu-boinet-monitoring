import argparse

from boinet_monitoring import events_reader


def build_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parse_commands(subparsers)

    return parser


def parse_commands(subparsers):
    parser = subparsers.add_parser("balances", help="Calculate balances per subject type")
    parser.set_defaults(func=events_reader.calculate_balances)
