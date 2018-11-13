from terminaltables import AsciiTable

from boinet_monitoring.BalanceCalculatorBySubjectType import BalanceCalculatorBySubjectType
from boinet_monitoring.BankAccountCalculator import BankAccountCalculator


class BalancesCalculator:

    def __init__(self):
        self.financial_events_processors = [BalanceCalculatorBySubjectType(subject_type)
                                            for subject_type
                                            in self.SUBJECT_TYPES] + [BankAccountCalculator()]
        header_row = ["Tick"] + self.SUBJECT_TYPES + ["Bank", "Total balance"]
        _print_table(header_row)

    def process_event(self, event):
        if "eventType" not in event:
            return self._process_tick(event)

        self._process_financial_event(event)

    def _process_financial_event(self, event):
        for processor in self.financial_events_processors:
            processor.process(event)

    def _process_tick(self, event):
        row = [event["tick"]] + self._balances_by_subject_type() + [self._total_balance()]
        _print_table(row)

    def _total_balance(self):
        return _prettify_money(sum([processor.get_summary() for processor in self.financial_events_processors]))

    def _balances_by_subject_type(self):
        return [_prettify_money(processor.get_summary()) for processor in self.financial_events_processors]

    SUBJECT_TYPES = ["PERSON", "COMPANY"]


def _print_table(row_data):
    table = AsciiTable([row_data])
    table.outer_border = False
    table.padding_left = 10
    table.padding_right = 2
    print(table.table)


def _prettify_money(amount):
    return "{0:,.0f}".format(amount) + " EUR"
