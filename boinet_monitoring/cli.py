import argparse
import threading

from boinet_monitoring import events_reader, terminal_printer
from boinet_monitoring.BalancesCalculator import BalancesCalculator
from boinet_monitoring.Plotter import Plotter


def build_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parse_commands(subparsers)

    return parser


def parse_commands(subparsers):
    parser = subparsers.add_parser("balances-table", help="Calculate balances per subject type in a table")
    parser.set_defaults(func=print_balances_table)

    parser = subparsers.add_parser("balances-graph", help="Calculate balances per subject type in a graph")
    parser.set_defaults(func=print_balances_graph)


def print_balances_table(_args):
    calculator = BalancesCalculator()

    return events_reader.read_events() \
        .map(calculator.accumulate) \
        .filter(lambda event_and_summary: "eventType" not in event_and_summary[0]) \
        .subscribe(lambda event_and_summary: terminal_printer.print_summary(event_and_summary[1]))


def print_balances_graph(_args):
    plotter = Plotter()

    t = threading.Thread(target=update_plotter(plotter))
    t.start()

    plotter.show()


def update_plotter(plotter):
    def read_events():
        calculator = BalancesCalculator()

        events_reader.read_events() \
            .map(calculator.accumulate) \
            .filter(lambda event_and_summary: "eventType" not in event_and_summary[0]) \
            .map(lambda event_and_summary: event_and_summary[1]) \
            .subscribe(lambda summary: plotter.on_data(summary[0], summary[1:4]))

    return read_events
